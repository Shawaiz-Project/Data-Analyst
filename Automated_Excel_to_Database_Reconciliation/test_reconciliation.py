"""Tests for the three-level reconciliation engine."""
import pandas as pd

from src import reconciliation


def _excel_df():
    return pd.DataFrame({
        "transaction_id": ["TX001", "TX002", "TX003"],
        "branch_id": ["BR001", "BR001", "BR002"],
        "transaction_date": pd.to_datetime(["2026-01-01"] * 3).date,
        "customer_id": ["C1", "C2", "C3"],
        "product_id": ["P1", "P2", "P3"],
        "quantity": [10, 5, 2],
        "unit_price": [100.0, 50.0, 25.0],
        "discount": [0.0, 0.0, 0.0],
        "revenue": [1000.0, 250.0, 50.0],
    })


def _db_df():
    """DB matches except: TX002 revenue 300 (vs 250), TX003 absent, TX999 extra."""
    return pd.DataFrame({
        "transaction_id": ["TX001", "TX002", "TX999"],
        "branch_id": ["BR001", "BR001", "BR002"],
        "transaction_date": pd.to_datetime(["2026-01-01"] * 3).date,
        "customer_id": ["C1", "C2", "C9"],
        "product_id": ["P1", "P2", "P9"],
        "quantity": [10, 5, 7],
        "unit_price": [100.0, 50.0, 10.0],
        "discount": [0.0, 0.0, 0.0],
        "revenue": [1000.0, 300.0, 70.0],
    })


# Test 5 — missing-from-database detection -----------------------------------
def test_missing_from_database_detected():
    txn = reconciliation.reconcile_transactions(_excel_df(), _db_df())
    missing = txn[txn["status"] == "MISSING_FROM_DATABASE"]
    assert list(missing["transaction_id"]) == ["TX003"]
    assert missing.iloc[0]["excel_value"] == "Present"
    assert missing.iloc[0]["db_value"] == "Missing"


def test_missing_from_excel_detected():
    txn = reconciliation.reconcile_transactions(_excel_df(), _db_df())
    extra = txn[txn["status"] == "MISSING_FROM_EXCEL"]
    assert list(extra["transaction_id"]) == ["TX999"]


def test_transaction_revenue_mismatch_detected():
    txn = reconciliation.reconcile_transactions(_excel_df(), _db_df())
    rev = txn[(txn["status"] == "REVENUE_MISMATCH")
              & (txn["transaction_id"] == "TX002")]
    assert len(rev) == 1
    assert rev.iloc[0]["excel_value"] == 250.0
    assert rev.iloc[0]["db_value"] == 300.0
    assert rev.iloc[0]["difference"] == -50.0


def test_global_reconciliation_totals():
    g = reconciliation.reconcile_global(_excel_df(), _db_df())
    assert g["excel_rows"] == 3 and g["db_rows"] == 3
    assert g["excel_revenue"] == 1300.0
    assert g["db_revenue"] == 1370.0
    assert g["revenue_diff"] == -70.0
    assert g["status"] == "FAIL"


def test_branch_reconciliation_statuses():
    b = reconciliation.reconcile_by_branch(_excel_df(), _db_df())
    br001 = b[b["branch_id"] == "BR001"].iloc[0]
    br002 = b[b["branch_id"] == "BR002"].iloc[0]
    assert br001["excel_revenue"] == 1250.0
    assert br001["db_revenue"] == 1300.0
    assert br001["status"] == "FAIL"     # TX002 revenue differs
    assert br002["status"] == "FAIL"     # TX003 missing, TX999 extra


def test_identical_data_passes_everywhere():
    df = _excel_df()
    g = reconciliation.reconcile_global(df, df.copy())
    b = reconciliation.reconcile_by_branch(df, df.copy())
    t = reconciliation.reconcile_transactions(df, df.copy())
    assert g["status"] == "PASS"
    assert (b["status"] == "PASS").all()
    assert t.empty
