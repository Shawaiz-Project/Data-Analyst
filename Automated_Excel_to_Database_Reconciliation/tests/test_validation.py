"""Tests for schema, missing-value, duplicate, type and revenue validation."""
import numpy as np
import pandas as pd
import pytest

from src import validation
from src.exceptions import SchemaValidationError

VALID_BRANCHES = ["BR001", "BR002", "BR003"]


def _base_df():
    """A minimal, fully valid dataframe (revenue obeys the rule)."""
    return pd.DataFrame({
        "transaction_id": ["TX001", "TX002", "TX003"],
        "branch_id": ["BR001", "BR002", "BR003"],
        "transaction_date": pd.to_datetime(["2026-01-01"] * 3),
        "customer_id": ["C1", "C2", "C3"],
        "product_id": ["P1", "P2", "P3"],
        "quantity": [10, 5, 2],
        "unit_price": [100.0, 50.0, 25.0],
        "discount": [0.0, 10.0, 0.0],
        "revenue": [1000.0, 240.0, 50.0],  # qty*price - discount
    })


# Test 1 — missing column => explicit SCHEMA_VALIDATION_FAILED -----------
def test_missing_column_raises_schema_error():
    df = pd.DataFrame({"transaction_id": ["TX001"],
                       "branch_id": ["BR001"],
                       "quantity": [1]})
    with pytest.raises(SchemaValidationError) as exc_info:
        validation.validate_schema(df)
    msg = str(exc_info.value)
    assert "SCHEMA_VALIDATION_FAILED" in msg
    assert "product_id" in exc_info.value.missing_columns
    assert "Pipeline stopped before database load." in msg


def test_unexpected_column_detected():
    df = _base_df()
    df["random_column"] = 1
    with pytest.raises(SchemaValidationError) as exc_info:
        validation.validate_schema(df)
    assert "random_column" in exc_info.value.unexpected_columns


def test_valid_schema_passes():
    result = validation.validate_schema(_base_df())
    assert result["status"] == "PASS"
    assert result["missing_columns"] == []
    assert result["unexpected_columns"] == []


# Test 2 — duplicate detection --------------------------------------------
def test_duplicate_detection():
    df = _base_df()
    df.loc[1, "transaction_id"] = "TX001"  # TX001, TX001, TX003
    dups = validation.detect_duplicates(df)
    assert set(dups["transaction_id"]) == {"TX001"}
    assert len(dups) == 2                    # keep=False flags both rows
    assert set(dups["error_type"]) == {"DUPLICATE_TRANSACTION"}
    # one duplicated id => exactly 1 duplicate GROUP
    assert dups["transaction_id"].nunique() == 1


# Test 3 — missing value categorisation ------------------------------------
def test_missing_branch_id_categorised():
    df = _base_df()
    df.loc[0, "branch_id"] = None
    exc = validation.validate_missing_values(df)
    assert "MISSING_BRANCH_ID" in set(exc["error_type"])
    assert exc[exc["error_type"] == "MISSING_BRANCH_ID"].iloc[0]["column"] == "branch_id"


def test_missing_transaction_id_categorised():
    df = _base_df()
    df.loc[2, "transaction_id"] = None
    exc = validation.validate_missing_values(df)
    assert "MISSING_TRANSACTION_ID" in set(exc["error_type"])


# Invalid numeric values preserve the ORIGINAL bad value -------------------
def test_invalid_numeric_preserves_original_value():
    df = _base_df()
    df["quantity"] = df["quantity"].astype(object)
    df.loc[1, "quantity"] = "ABC"
    clean, exc = validation.validate_types(df)
    bad = exc[exc["error_type"] == "INVALID_INTEGER_VALUE"]
    assert len(bad) == 1
    assert bad.iloc[0]["original_value"] == "ABC"
    assert bad.iloc[0]["column"] == "quantity"
    assert pd.isna(clean.loc[1, "quantity"])  # coerced but RECORDED


def test_invalid_date_detected():
    df = _base_df()
    # Excel cells are untyped; simulate a text value landing in the date
    # column by holding the column as object (as read from a messy file).
    df["transaction_date"] = df["transaction_date"].astype(object)
    df.loc[0, "transaction_date"] = "not-a-date"
    _, exc = validation.validate_types(df)
    assert "INVALID_DATE_VALUE" in set(exc["error_type"])


# Test 4 — revenue mismatch against the business rule ----------------------
def test_revenue_mismatch_detected():
    df = _base_df()
    # quantity=10, unit_price=100, discount=0 => expected 1000, reported 900
    df.loc[0, "revenue"] = 900.0
    exc = validation.validate_revenue(df)
    assert len(exc) == 1
    assert exc.iloc[0]["error_type"] == "REVENUE_MISMATCH"
    assert exc.iloc[0]["transaction_id"] == "TX001"


def test_revenue_rule_within_tolerance_passes():
    df = _base_df()
    df.loc[0, "revenue"] = 1000.02  # within 0.05 tolerance
    assert validation.validate_revenue(df).empty


# Invalid branch detection ---------------------------------------------------
def test_invalid_branch_detected():
    df = _base_df()
    df.loc[0, "branch_id"] = "BR999"
    exc = validation.validate_branches(df, VALID_BRANCHES)
    assert len(exc) == 1
    assert exc.iloc[0]["error_type"] == "INVALID_BRANCH"
    assert exc.iloc[0]["original_value"] == "BR999"


# Full orchestration: valid/invalid split ------------------------------------
def test_run_all_validations_splits_rows():
    df = _base_df()
    df.loc[0, "branch_id"] = None            # missing value  -> invalid
    df.loc[1, "revenue"] = 1.0               # revenue mismatch -> invalid
    valid, invalid, exc, stats = validation.run_all_validations(
        df, VALID_BRANCHES)
    assert stats["input_rows"] == 3
    assert stats["valid_rows"] == 1
    assert stats["invalid_rows"] == 2
    assert list(valid["transaction_id"]) == ["TX003"]
    assert len(exc) >= 2
