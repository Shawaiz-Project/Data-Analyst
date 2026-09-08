"""Transform step — normalise validated records for database loading.

Only VALID records reach this module. It produces a load-ready dataframe
with canonical dtypes and (optionally) the run id stamped on each row.
"""
import pandas as pd

from . import config


def to_load_frame(valid_df: pd.DataFrame, run_id: str | None = None) -> pd.DataFrame:
    """Return a clean, load-ready copy of the validated records."""
    df = valid_df[config.EXPECTED_COLUMNS].copy()

    for col in config.ID_COLUMNS:
        df[col] = df[col].astype("string").str.strip()

    df["transaction_date"] = pd.to_datetime(df["transaction_date"]).dt.date
    df["quantity"] = df["quantity"].astype("int64")
    for col in config.NUMERIC_COLUMNS:
        df[col] = df[col].astype("float64").round(2)

    if run_id is not None:
        df["loaded_run_id"] = run_id
    return df


def aggregate_totals(df: pd.DataFrame) -> dict:
    """Global totals used by the reconciliation engine."""
    return {
        "rows": int(len(df)),
        "quantity": float(df["quantity"].sum()) if len(df) else 0.0,
        "revenue": round(float(df["revenue"].sum()), 2) if len(df) else 0.0,
    }
