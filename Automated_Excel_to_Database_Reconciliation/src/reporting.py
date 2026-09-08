"""Phase — reporting: exception.xlsx and validation_report.xlsx.

exception.xlsx worksheets (section 28):
    Summary | Schema_Errors | Missing_Values | Duplicates | Invalid_Types |
    Revenue_Mismatches | Missing_Transactions | Extra_Transactions |
    Branch_Reconciliation
"""
from __future__ import annotations

from datetime import datetime
from pathlib import Path

import pandas as pd
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

from . import config

HEADER_FILL = PatternFill("solid", fgColor="1F4E78")
HEADER_FONT = Font(color="FFFFFF", bold=True)
PASS_FILL = PatternFill("solid", fgColor="C6EFCE")
FAIL_FILL = PatternFill("solid", fgColor="FFC7CE")


def _autosize_and_style(writer, sheet_name: str) -> None:
    ws = writer.sheets[sheet_name]
    for row in ws.iter_rows(min_row=1, max_row=1):
        for cell in row:
            cell.fill = HEADER_FILL
            cell.font = HEADER_FONT
            cell.alignment = Alignment(vertical="center")
    for col_idx, column_cells in enumerate(ws.columns, start=1):
        length = max((len(str(c.value)) for c in column_cells if c.value is not None),
                     default=8)
        ws.column_dimensions[get_column_letter(col_idx)].width = min(length + 3, 60)
    ws.freeze_panes = "A2"


def _filter_exc(exceptions_df: pd.DataFrame, error_types) -> pd.DataFrame:
    if exceptions_df.empty:
        return exceptions_df
    return exceptions_df[exceptions_df["error_type"].isin(error_types)]


def write_exception_workbook(path: Path, run_id: str, stats: dict,
                             exceptions_df: pd.DataFrame,
                             branch_recon_df: pd.DataFrame,
                             txn_mismatch_df: pd.DataFrame,
                             schema_error: dict | None = None,
                             logger=None) -> Path:
    """Generate reports/exception.xlsx (mandatory deliverable)."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    # ---- Summary sheet (section 29) ------------------------------------
    summary_rows = [
        ("Run ID", run_id),
        ("Generated At", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        ("Dataset", "Synthetic Dataset — Not Real Financial Data"),
        ("Input Rows", stats.get("input_rows", 0)),
        ("Valid Rows", stats.get("valid_rows", 0)),
        ("Invalid Rows", stats.get("invalid_rows", 0)),
        ("Duplicate Rows", stats.get("duplicate_rows", 0)),
        ("Missing Values", stats.get("missing_values", 0)),
        ("Invalid Types", stats.get("invalid_types", 0)),
        ("Invalid Branches", stats.get("invalid_branches", 0)),
        ("Revenue Mismatches", stats.get("revenue_mismatches", 0)),
        ("Branches Checked", stats.get("branches_checked", 0)),
        ("Branches Passed", stats.get("branches_passed", 0)),
        ("Branches Failed", stats.get("branches_failed", 0)),
        ("Transaction Mismatches", stats.get("transaction_mismatches", 0)),
        ("Data Quality Score", stats.get("dq_score", "")),
        ("DQ Rating", stats.get("dq_rating", "")),
        ("Overall Status", stats.get("overall_status", "")),
    ]
    summary_df = pd.DataFrame(summary_rows, columns=["Metric", "Count"])

    schema_df = pd.DataFrame(
        [{"error_type": "SCHEMA_VALIDATION_FAILED",
          "missing_columns": ", ".join(schema_error.get("missing_columns", [])),
          "unexpected_columns": ", ".join(schema_error.get("unexpected_columns", []))}]
        if schema_error else [],
        columns=["error_type", "missing_columns", "unexpected_columns"])

    missing_from_db = txn_mismatch_df[txn_mismatch_df["status"] == "MISSING_FROM_DATABASE"]
    extra_in_db = txn_mismatch_df[txn_mismatch_df["status"] == "MISSING_FROM_EXCEL"]

    with pd.ExcelWriter(path, engine="openpyxl") as writer:
        summary_df.to_excel(writer, sheet_name="Summary", index=False)
        schema_df.to_excel(writer, sheet_name="Schema_Errors", index=False)
        _filter_exc(exceptions_df, [v for v in config.CRITICAL_FIELDS.values()]
                    ).to_excel(writer, sheet_name="Missing_Values", index=False)
        _filter_exc(exceptions_df, ["DUPLICATE_TRANSACTION"]
                    ).to_excel(writer, sheet_name="Duplicates", index=False)
        _filter_exc(exceptions_df, ["INVALID_INTEGER_VALUE",
                                    "INVALID_NUMERIC_VALUE",
                                    "INVALID_DATE_VALUE", "INVALID_BRANCH"]
                    ).to_excel(writer, sheet_name="Invalid_Types", index=False)
        _filter_exc(exceptions_df, ["REVENUE_MISMATCH"]
                    ).to_excel(writer, sheet_name="Revenue_Mismatches", index=False)
        missing_from_db.to_excel(writer, sheet_name="Missing_Transactions", index=False)
        extra_in_db.to_excel(writer, sheet_name="Extra_Transactions", index=False)
        branch_recon_df.to_excel(writer, sheet_name="Branch_Reconciliation", index=False)

        for sheet in writer.sheets:
            _autosize_and_style(writer, sheet)

        # colour-code PASS/FAIL in Branch_Reconciliation and Summary
        ws = writer.sheets["Branch_Reconciliation"]
        status_col = list(branch_recon_df.columns).index("status") + 1
        for r in range(2, ws.max_row + 1):
            cell = ws.cell(row=r, column=status_col)
            cell.fill = PASS_FILL if cell.value == "PASS" else FAIL_FILL

    if logger:
        logger.info("Exception report written | %s", path)
    return path


def write_validation_report(path: Path, run_id: str,
                            stage_statuses: list[tuple[str, str, str]],
                            stats: dict, logger=None) -> Path:
    """Generate reports/validation_report.xlsx with PASS/FAIL per stage and
    the overall READY_FOR_FINANCE_SIGNOFF / REQUIRES_INVESTIGATION verdict."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    status_df = pd.DataFrame(stage_statuses,
                             columns=["Stage", "Status", "Detail"])
    metrics_df = pd.DataFrame(
        [(k, v) for k, v in stats.items()],
        columns=["Metric", "Value"])

    with pd.ExcelWriter(path, engine="openpyxl") as writer:
        status_df.to_excel(writer, sheet_name="Validation_Status", index=False)
        metrics_df.to_excel(writer, sheet_name="Run_Metrics", index=False)
        for sheet in writer.sheets:
            _autosize_and_style(writer, sheet)
        ws = writer.sheets["Validation_Status"]
        for r in range(2, ws.max_row + 1):
            cell = ws.cell(row=r, column=2)
            if cell.value in ("PASS", "READY_FOR_FINANCE_SIGNOFF"):
                cell.fill = PASS_FILL
            elif cell.value in ("FAIL", "REQUIRES_INVESTIGATION"):
                cell.fill = FAIL_FILL

    if logger:
        logger.info("Validation report written | %s", path)
    return path


def compute_dq_score(stats: dict) -> tuple[float, str]:
    """Advanced Extension (Option E) — Data Quality Score.

    score = 100
            - 1.0 per duplicate row          per 1,000 input rows
            - 1.5 per missing value          per 1,000 input rows
            - 2.0 per invalid type           per 1,000 input rows
            - 2.0 per revenue mismatch       per 1,000 input rows
            - 2.5 per invalid branch         per 1,000 input rows
            - 10.0 flat if any branch fails reconciliation
    """
    n = max(stats.get("input_rows", 0), 1) / 1000.0
    penalty = (
        config.DQ_PENALTY_PER_1000["DUPLICATE_TRANSACTION"] * stats.get("duplicate_rows", 0) / n
        + config.DQ_PENALTY_PER_1000["MISSING_VALUE"] * stats.get("missing_values", 0) / n
        + config.DQ_PENALTY_PER_1000["INVALID_TYPE"] * stats.get("invalid_types", 0) / n
        + config.DQ_PENALTY_PER_1000["REVENUE_MISMATCH"] * stats.get("revenue_mismatches", 0) / n
        + config.DQ_PENALTY_PER_1000["INVALID_BRANCH"] * stats.get("invalid_branches", 0) / n
    )
    if stats.get("branches_failed", 0) > 0:
        penalty += config.DQ_RECONCILIATION_PENALTY
    score = max(0.0, round(100.0 - penalty, 1))
    rating = ("Excellent" if score >= 95 else
              "Good" if score >= 90 else
              "Warning" if score >= 75 else "Failed")
    return score, rating
