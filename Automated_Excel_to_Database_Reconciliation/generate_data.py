#!/usr/bin/env python3
"""Phase 1 — Synthetic data generator.

Generates a 30,000-row synthetic branch sales workbook at
data/input/branch_sales.xlsx with intentional defects (section 6).

    Synthetic Dataset — Not Real Financial Data

Revenue business rule (section 12):
    gross_amount = quantity * unit_price
    revenue      = gross_amount - discount

The workbook contains 6 sheets:
    Branch_Sales    — the branch submission WITH injected defects
    Canonical_Sales — the official database export (clean source of truth)
    Branches / Customers / Products — dimension tables
    Dataset_Info    — defect inventory (self-documenting)
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from src import config  # noqa: E402

RNG = np.random.default_rng(seed=42)
N_ROWS = 30_000
N_BRANCHES, N_CUSTOMERS, N_PRODUCTS = 10, 3_000, 500
DATE_START, DATE_END = "2026-01-01", "2026-08-31"

# Defect counts (section 6)
N_DUPLICATES = 50
N_MISSING = 50
N_INVALID_NUMERIC = 25
N_WRONG_REVENUE = 25
N_INVALID_BRANCH = 20
N_REMOVED_FROM_EXCEL = 20  # canonical transactions the branch "forgot"


def build_dimensions():
    branches = pd.DataFrame({
        "branch_id": [f"BR{i:03d}" for i in range(1, N_BRANCHES + 1)],
        "branch_name": [f"Branch {i:03d}" for i in range(1, N_BRANCHES + 1)],
    })
    customers = pd.DataFrame({
        "customer_id": [f"CUST{i:05d}" for i in range(1, N_CUSTOMERS + 1)],
        "customer_name": [f"Customer {i:05d}" for i in range(1, N_CUSTOMERS + 1)],
    })
    categories = ["Grocery", "Electronics", "Apparel", "Home", "Beauty"]
    products = pd.DataFrame({
        "product_id": [f"PROD{i:04d}" for i in range(1, N_PRODUCTS + 1)],
        "product_name": [f"Product {i:04d}" for i in range(1, N_PRODUCTS + 1)],
        "category": RNG.choice(categories, N_PRODUCTS),
    })
    return branches, customers, products


def build_clean_sales(branches, customers, products) -> pd.DataFrame:
    """The clean canonical dataset — revenue always obeys the rule."""
    n = N_ROWS
    quantity = RNG.integers(1, 11, n)
    unit_price = np.round(RNG.uniform(5, 1_000, n), 2)
    discount = np.round(RNG.uniform(0, 100, n), 2)
    discount = np.minimum(discount, quantity * unit_price)  # keep revenue >= 0
    revenue = np.round(quantity * unit_price - discount, 2)

    dates = pd.to_datetime(DATE_START) + pd.to_timedelta(
        RNG.integers(0, (pd.Timestamp(DATE_END) - pd.Timestamp(DATE_START)).days + 1, n),
        unit="D")

    return pd.DataFrame({
        "transaction_id": [f"TXN{i:07d}" for i in range(1, n + 1)],
        "branch_id": RNG.choice(branches["branch_id"], n),
        "transaction_date": dates,
        "customer_id": RNG.choice(customers["customer_id"], n),
        "product_id": RNG.choice(products["product_id"], n),
        "quantity": quantity,
        "unit_price": unit_price,
        "discount": discount,
        "revenue": revenue,
    })


def inject_defects(canonical: pd.DataFrame, valid_branch_ids):
    """Return the branch submission = canonical + intentional defects."""
    df = canonical.copy()
    defect_counts = {}

    # 1. Duplicate transactions (50 extra rows, ids duplicated)
    dup_idx = RNG.choice(df.index, N_DUPLICATES, replace=False)
    df = pd.concat([df, df.loc[dup_idx]], ignore_index=True)
    defect_counts["Duplicate source rows"] = N_DUPLICATES

    # 2. Missing values in critical fields
    miss_fields = ["transaction_id", "branch_id", "product_id",
                   "quantity", "unit_price", "revenue"]
    miss_idx = RNG.choice(df.index, N_MISSING, replace=False)
    for i, idx in enumerate(miss_idx):
        df.loc[idx, miss_fields[i % len(miss_fields)]] = np.nan
    defect_counts["Missing-value cases"] = N_MISSING

    # 3. Invalid numeric values ("ABC", "N/A", ...) — cast to object first
    bad_tokens = ["ABC", "N/A", "err", "#VALUE!", "--"]
    df["quantity"] = df["quantity"].astype(object)
    df["unit_price"] = df["unit_price"].astype(object)
    inv_idx = RNG.choice(df.index, N_INVALID_NUMERIC, replace=False)
    for i, idx in enumerate(inv_idx):
        col = "quantity" if i % 2 == 0 else "unit_price"
        df.loc[idx, col] = bad_tokens[i % len(bad_tokens)]
    defect_counts["Invalid numeric/type cases"] = N_INVALID_NUMERIC

    # 4. Incorrect revenue (breaks the revenue rule)
    rev_idx = RNG.choice(df.index, N_WRONG_REVENUE, replace=False)
    df["revenue"] = df["revenue"].astype(object)
    for idx in rev_idx:
        try:
            df.loc[idx, "revenue"] = round(float(df.loc[idx, "revenue"])
                                           + RNG.uniform(50, 500), 2)
        except (TypeError, ValueError):
            df.loc[idx, "revenue"] = 9999.99
    defect_counts["Incorrect revenue cases"] = N_WRONG_REVENUE

    # 5. Invalid branch ids (not in the canonical branch table)
    br_idx = RNG.choice(df.index, N_INVALID_BRANCH, replace=False)
    for i, idx in enumerate(br_idx):
        df.loc[idx, "branch_id"] = f"BR{900 + i:03d}"
    defect_counts["Invalid branch cases"] = N_INVALID_BRANCH

    # 6. Removed transactions — present in canonical DB, absent from Excel
    removed_ids = RNG.choice(canonical["transaction_id"],
                             N_REMOVED_FROM_EXCEL, replace=False)
    df = df[~df["transaction_id"].isin(removed_ids)].reset_index(drop=True)
    defect_counts["Removed transaction cases"] = N_REMOVED_FROM_EXCEL

    # Shuffle so defects are not grouped
    df = df.sample(frac=1.0, random_state=42).reset_index(drop=True)
    return df, defect_counts


def main() -> None:
    config.DATA_INPUT_DIR.mkdir(parents=True, exist_ok=True)
    config.DATA_CANONICAL_DIR.mkdir(parents=True, exist_ok=True)

    branches, customers, products = build_dimensions()
    canonical = build_clean_sales(branches, customers, products)
    submission, defect_counts = inject_defects(canonical, branches["branch_id"])

    # Canonical CSVs used by the pipeline
    canonical.to_csv(config.CANONICAL_SALES_CSV, index=False)
    branches.to_csv(config.BRANCHES_CSV, index=False)
    customers.to_csv(config.CUSTOMERS_CSV, index=False)
    products.to_csv(config.PRODUCTS_CSV, index=False)

    info = pd.DataFrame({
        "item": ["Dataset label", "Base canonical rows", "Submission rows",
                 *defect_counts.keys(),
                 "Branches", "Customers", "Products",
                 "Date start", "Date end", "Revenue rule"],
        "value": ["SYNTHETIC — FOR EDUCATIONAL USE ONLY",
                  len(canonical), len(submission),
                  *defect_counts.values(),
                  N_BRANCHES, N_CUSTOMERS, N_PRODUCTS,
                  DATE_START, DATE_END,
                  "revenue = quantity × unit_price − discount"],
    })

    with pd.ExcelWriter(config.EXCEL_FILE, engine="openpyxl") as writer:
        submission.to_excel(writer, sheet_name="Branch_Sales", index=False)
        branches.to_excel(writer, sheet_name="Branches", index=False)
        customers.to_excel(writer, sheet_name="Customers", index=False)
        products.to_excel(writer, sheet_name="Products", index=False)
        canonical.to_excel(writer, sheet_name="Canonical_Sales", index=False)
        info.to_excel(writer, sheet_name="Dataset_Info", index=False)

    print("Synthetic Dataset — Not Real Financial Data")
    print(f"Workbook written : {config.EXCEL_FILE}")
    print(f"Submission rows  : {len(submission):,}")
    print(f"Canonical rows   : {len(canonical):,}")
    for k, v in defect_counts.items():
        print(f"  {k:<28}: {v}")


if __name__ == "__main__":
    main()
