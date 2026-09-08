"""Phases 3–6 & 12 — schema, type, missing-value, duplicate, branch and
revenue validation.

Every check appends rows to a shared *exceptions* dataframe with columns:
    row_number | transaction_id | column | error_type | original_value | detail
so nothing is ever silently coerced or dropped.
"""
import numpy as np
import pandas as pd

from . import config
from .exceptions import SchemaValidationError

EXCEPTION_COLUMNS = ["row_number", "transaction_id", "column",
                     "error_type", "original_value", "detail"]


# ---------------------------------------------------------------------------
# Phase 3 — Schema validation
# ---------------------------------------------------------------------------
def validate_schema(df: pd.DataFrame, expected_columns=None,
                    logger=None) -> dict:
    """Check required, missing and unexpected columns.

    Returns a result dict; raises SchemaValidationError on failure so the
    pipeline stops *before* any database load (section 15)."""
    expected = list(expected_columns or config.EXPECTED_COLUMNS)
    actual = list(df.columns)
    missing = [c for c in expected if c not in actual]
    unexpected = [c for c in actual if c not in expected]

    result = {"status": "PASS" if not missing and not unexpected else "FAIL",
              "missing_columns": missing,
              "unexpected_columns": unexpected}

    if result["status"] == "FAIL":
        if logger:
            logger.error("Schema validation FAILED | missing=%s unexpected=%s",
                         missing, unexpected)
        raise SchemaValidationError(missing, unexpected)

    if logger:
        logger.info("Schema validation passed | columns=%d", len(actual))
    return result


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _empty_exceptions() -> pd.DataFrame:
    return pd.DataFrame(columns=EXCEPTION_COLUMNS)


def _make_exception_row(idx, txn_id, column, error_type,
                        original_value, detail) -> dict:
    return {"row_number": int(idx) + 2,  # +2: header row + 0-based index
            "transaction_id": txn_id,
            "column": column,
            "error_type": error_type,
            "original_value": None if pd.isna(original_value) else original_value,
            "detail": detail}


# ---------------------------------------------------------------------------
# Phase 4 — Data type validation (records original bad values — section 17)
# ---------------------------------------------------------------------------
def validate_types(df: pd.DataFrame, logger=None):
    """Validate / normalise column types.

    Returns (clean_df, exceptions_df). Numeric/date coercion failures keep
    the ORIGINAL value in the exception report — never a silent NaN."""
    df = df.copy()
    exceptions = []

    # Identifier columns -> trimmed strings (empty strings become NaN)
    for col in config.ID_COLUMNS:
        if col in df.columns:
            df[col] = df[col].astype("string").str.strip()
            df[col] = df[col].replace({"": pd.NA})

    # Integer columns
    for col in config.INTEGER_COLUMNS:
        if col not in df.columns:
            continue
        numeric = pd.to_numeric(df[col], errors="coerce")
        bad_mask = numeric.isna() & df[col].notna()
        for idx in df.index[bad_mask]:
            exceptions.append(_make_exception_row(
                idx, df.at[idx, "transaction_id"], col,
                "INVALID_INTEGER_VALUE", df.at[idx, col],
                f"Value '{df.at[idx, col]}' is not a valid integer"))
        df[col] = numeric.astype("Int64")

    # Numeric columns
    for col in config.NUMERIC_COLUMNS:
        if col not in df.columns:
            continue
        numeric = pd.to_numeric(df[col], errors="coerce")
        bad_mask = numeric.isna() & df[col].notna()
        for idx in df.index[bad_mask]:
            exceptions.append(_make_exception_row(
                idx, df.at[idx, "transaction_id"], col,
                "INVALID_NUMERIC_VALUE", df.at[idx, col],
                f"Value '{df.at[idx, col]}' is not a valid number"))
        df[col] = numeric.astype("Float64")

    # Date columns
    for col in config.DATE_COLUMNS:
        if col not in df.columns:
            continue
        parsed = pd.to_datetime(df[col], errors="coerce")
        bad_mask = parsed.isna() & df[col].notna()
        for idx in df.index[bad_mask]:
            exceptions.append(_make_exception_row(
                idx, df.at[idx, "transaction_id"], col,
                "INVALID_DATE_VALUE", df.at[idx, col],
                f"Value '{df.at[idx, col]}' is not a valid date"))
        df[col] = parsed

    exc_df = pd.DataFrame(exceptions, columns=EXCEPTION_COLUMNS)
    if logger:
        logger.info("Type validation completed | invalid_types=%d", len(exc_df))
    return df, exc_df


# ---------------------------------------------------------------------------
# Phase 5 — Missing-value validation (categorised, section 18)
# ---------------------------------------------------------------------------
def validate_missing_values(df: pd.DataFrame,
                            critical_fields: dict | None = None,
                            logger=None) -> pd.DataFrame:
    """Detect nulls in critical fields; each error is categorised
    (MISSING_TRANSACTION_ID, MISSING_BRANCH_ID, ...)."""
    critical_fields = critical_fields or config.CRITICAL_FIELDS
    exceptions = []
    for col, error_type in critical_fields.items():
        if col not in df.columns:
            continue
        null_mask = df[col].isna()
        for idx in df.index[null_mask]:
            exceptions.append(_make_exception_row(
                idx, df.at[idx, "transaction_id"], col,
                error_type, None, f"Critical field '{col}' is missing"))

    exc_df = pd.DataFrame(exceptions, columns=EXCEPTION_COLUMNS)
    if logger:
        logger.warning("missing_values=%d", len(exc_df))
    return exc_df


# ---------------------------------------------------------------------------
# Phase 6 — Duplicate detection (keep=False flags every occurrence)
# ---------------------------------------------------------------------------
def detect_duplicates(df: pd.DataFrame, logger=None) -> pd.DataFrame:
    """Flag every occurrence of a duplicated transaction_id."""
    if "transaction_id" not in df.columns:
        return _empty_exceptions()
    has_id = df["transaction_id"].notna()
    dup_mask = has_id & df["transaction_id"].duplicated(keep=False)
    exceptions = [
        _make_exception_row(idx, df.at[idx, "transaction_id"],
                            "transaction_id", "DUPLICATE_TRANSACTION",
                            df.at[idx, "transaction_id"],
                            "transaction_id appears more than once in the submission")
        for idx in df.index[dup_mask]
    ]
    exc_df = pd.DataFrame(exceptions, columns=EXCEPTION_COLUMNS)
    if logger:
        logger.warning("duplicates=%d", len(exc_df))
    return exc_df


# ---------------------------------------------------------------------------
# Branch referential validation — invalid branch IDs (section 6)
# ---------------------------------------------------------------------------
def validate_branches(df: pd.DataFrame, valid_branch_ids, logger=None) -> pd.DataFrame:
    """Flag rows whose branch_id is not in the canonical branch table."""
    if "branch_id" not in df.columns:
        return _empty_exceptions()
    mask = df["branch_id"].notna() & ~df["branch_id"].isin(set(valid_branch_ids))
    exceptions = [
        _make_exception_row(idx, df.at[idx, "transaction_id"],
                            "branch_id", "INVALID_BRANCH",
                            df.at[idx, "branch_id"],
                            f"branch_id '{df.at[idx, 'branch_id']}' does not exist "
                            "in the canonical branch table")
        for idx in df.index[mask]
    ]
    exc_df = pd.DataFrame(exceptions, columns=EXCEPTION_COLUMNS)
    if logger:
        logger.warning("invalid_branches=%d", len(exc_df))
    return exc_df


# ---------------------------------------------------------------------------
# Phase 12 — Revenue rule validation: revenue = quantity*unit_price - discount
# ---------------------------------------------------------------------------
def validate_revenue(df: pd.DataFrame,
                     tolerance: float = config.REVENUE_TOLERANCE,
                     logger=None) -> pd.DataFrame:
    """Check reported revenue against the business rule within a decimal
    tolerance. Rows with missing components are skipped (already reported
    as missing values)."""
    required = {"quantity", "unit_price", "discount", "revenue"}
    if not required.issubset(df.columns):
        return _empty_exceptions()

    complete = df[["quantity", "unit_price", "discount", "revenue"]].notna().all(axis=1)
    expected = (df["quantity"].astype("Float64") * df["unit_price"].astype("Float64")
                - df["discount"].astype("Float64"))
    diff = (df["revenue"].astype("Float64") - expected).abs()
    mismatch = complete & (diff > tolerance)

    exceptions = []
    for idx in df.index[mismatch]:
        exceptions.append(_make_exception_row(
            idx, df.at[idx, "transaction_id"], "revenue",
            "REVENUE_MISMATCH", df.at[idx, "revenue"],
            f"reported={df.at[idx, 'revenue']} expected={round(float(expected.loc[idx]), 2)} "
            f"(quantity*unit_price-discount)"))

    exc_df = pd.DataFrame(exceptions, columns=EXCEPTION_COLUMNS)
    if logger:
        logger.warning("revenue_mismatches=%d", len(exc_df))
    return exc_df


# ---------------------------------------------------------------------------
# Orchestration — run all checks, split valid vs invalid
# ---------------------------------------------------------------------------
def run_all_validations(df: pd.DataFrame, valid_branch_ids, logger=None):
    """Run every validation check and return
    (valid_df, invalid_df, exceptions_df, stats_dict)."""
    clean_df, type_exc = validate_types(df, logger=logger)
    missing_exc = validate_missing_values(clean_df, logger=logger)
    dup_exc = detect_duplicates(clean_df, logger=logger)
    branch_exc = validate_branches(clean_df, valid_branch_ids, logger=logger)
    revenue_exc = validate_revenue(clean_df, logger=logger)

    exceptions_df = pd.concat(
        [type_exc, missing_exc, dup_exc, branch_exc, revenue_exc],
        ignore_index=True)

    # A row is invalid if it has ANY data-quality error. Duplicated
    # transaction_ids are invalid too — the canonical DB enforces one row
    # per transaction, so every occurrence is quarantined.
    if len(exceptions_df):
        bad_rows = set(exceptions_df["row_number"])  # Excel row numbers (+2)
        invalid_mask = clean_df.index.map(lambda i: (i + 2) in bad_rows)
    else:
        invalid_mask = pd.Series(False, index=clean_df.index)

    invalid_df = clean_df[invalid_mask].copy()
    valid_df = clean_df[~invalid_mask].copy()

    stats = {
        "input_rows": len(clean_df),
        "valid_rows": len(valid_df),
        "invalid_rows": len(invalid_df),
        "duplicate_rows": int(len(dup_exc)),
        "missing_values": int(len(missing_exc)),
        "invalid_types": int(len(type_exc)),
        "invalid_branches": int(len(branch_exc)),
        "revenue_mismatches": int(len(revenue_exc)),
    }
    return valid_df, invalid_df, exceptions_df, stats
