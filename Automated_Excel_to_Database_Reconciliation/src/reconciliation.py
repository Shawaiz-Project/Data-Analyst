"""Phase 9 — three-level reconciliation engine (section 38).

LEVEL 1  Global      : total rows / quantity / revenue
LEVEL 2  Branch      : per-branch rows / quantity / revenue
LEVEL 3  Transaction : missing-from-db, missing-from-excel, and
                       field-level (quantity / unit_price / revenue) diffs
"""
from __future__ import annotations

import pandas as pd

RECON_COLUMNS = ["level", "branch_id", "excel_rows", "db_rows", "row_diff",
                 "excel_quantity", "db_quantity", "quantity_diff",
                 "excel_revenue", "db_revenue", "revenue_diff", "status"]

TOLERANCE = 0.05


def _agg(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"rows": 0, "quantity": 0.0, "revenue": 0.0}
    return {"rows": int(len(df)),
            "quantity": float(df["quantity"].sum()),
            "revenue": round(float(df["revenue"].sum()), 2)}


def _recon_row(level: str, branch_id: str,
               excel: dict, db: dict) -> dict:
    row_diff = excel["rows"] - db["rows"]
    qty_diff = round(excel["quantity"] - db["quantity"], 2)
    rev_diff = round(excel["revenue"] - db["revenue"], 2)
    status = "PASS" if (row_diff == 0 and abs(qty_diff) <= TOLERANCE
                        and abs(rev_diff) <= TOLERANCE) else "FAIL"
    return {"level": level, "branch_id": branch_id,
            "excel_rows": excel["rows"], "db_rows": db["rows"],
            "row_diff": row_diff,
            "excel_quantity": excel["quantity"],
            "db_quantity": db["quantity"], "quantity_diff": qty_diff,
            "excel_revenue": excel["revenue"], "db_revenue": db["revenue"],
            "revenue_diff": rev_diff, "status": status}


def reconcile_global(excel_df: pd.DataFrame, db_df: pd.DataFrame) -> dict:
    """LEVEL 1 — global totals."""
    return _recon_row("GLOBAL", "__ALL__", _agg(excel_df), _agg(db_df))


def reconcile_by_branch(excel_df: pd.DataFrame,
                        db_df: pd.DataFrame) -> pd.DataFrame:
    """LEVEL 2 — per-branch reconciliation (outer join on branch_id so a
    branch present on only one side is still reported)."""
    branch_ids = sorted(set(excel_df["branch_id"].dropna())
                        | set(db_df["branch_id"].dropna()))
    rows = []
    for bid in branch_ids:
        e = excel_df[excel_df["branch_id"] == bid]
        d = db_df[db_df["branch_id"] == bid]
        rows.append(_recon_row("BRANCH", bid, _agg(e), _agg(d)))
    return pd.DataFrame(rows, columns=RECON_COLUMNS)


def reconcile_transactions(excel_df: pd.DataFrame,
                           db_df: pd.DataFrame,
                           tolerance: float = TOLERANCE) -> pd.DataFrame:
    """LEVEL 3 — transaction-level mismatches.

    Detects:  MISSING_FROM_DATABASE, MISSING_FROM_EXCEL,
              QUANTITY_MISMATCH, PRICE_MISMATCH, REVENUE_MISMATCH.
    """
    e = excel_df.set_index("transaction_id")
    d = db_df.set_index("transaction_id")

    excel_ids = set(e.index)
    db_ids = set(d.index)
    records = []

    # In Excel but not in the canonical database
    for txn in sorted(excel_ids - db_ids):
        records.append({"transaction_id": txn, "field": "transaction",
                        "excel_value": "Present", "db_value": "Missing",
                        "difference": None, "status": "MISSING_FROM_DATABASE"})

    # In the canonical database but absent from the Excel submission
    for txn in sorted(db_ids - excel_ids):
        records.append({"transaction_id": txn, "field": "transaction",
                        "excel_value": "Missing", "db_value": "Present",
                        "difference": None, "status": "MISSING_FROM_EXCEL"})

    # Field-level comparison for shared transactions
    common = sorted(excel_ids & db_ids)
    fields = [("quantity", "QUANTITY_MISMATCH"),
              ("unit_price", "PRICE_MISMATCH"),
              ("revenue", "REVENUE_MISMATCH")]
    if common:
        ec = e.loc[common]
        dc = d.loc[common]
        for field, label in fields:
            ev = pd.to_numeric(ec[field], errors="coerce")
            dv = pd.to_numeric(dc[field], errors="coerce")
            diff = (ev - dv).abs()
            mismatch = diff > tolerance
            for txn in ec.index[mismatch.fillna(False)]:
                records.append({
                    "transaction_id": txn, "field": field,
                    "excel_value": float(ev.loc[txn]),
                    "db_value": float(dv.loc[txn]),
                    "difference": round(float(ev.loc[txn] - dv.loc[txn]), 2),
                    "status": label})

    cols = ["transaction_id", "field", "excel_value", "db_value",
            "difference", "status"]
    return pd.DataFrame(records, columns=cols)


def run_reconciliation(excel_df: pd.DataFrame, db_df: pd.DataFrame,
                       logger=None):
    """Run all three levels. Returns
    (global_row_dict, branch_df, transaction_df, summary_dict)."""
    global_row = reconcile_global(excel_df, db_df)
    branch_df = reconcile_by_branch(excel_df, db_df)
    txn_df = reconcile_transactions(excel_df, db_df)

    summary = {
        "branches_checked": int(len(branch_df)),
        "branches_passed": int((branch_df["status"] == "PASS").sum()),
        "branches_failed": int((branch_df["status"] == "FAIL").sum()),
        "transaction_mismatches": int(len(txn_df)),
        "global_status": global_row["status"],
    }
    if logger:
        logger.info("Reconciliation completed | branches_passed=%d/%d "
                    "txn_mismatches=%d", summary["branches_passed"],
                    summary["branches_checked"],
                    summary["transaction_mismatches"])
    return global_row, branch_df, txn_df, summary
