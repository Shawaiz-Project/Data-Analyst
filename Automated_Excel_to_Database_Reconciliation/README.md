# Day 6 — Automated Excel-to-Database Reconciliation

> **Synthetic Dataset — Not Real Financial Data.** All records in this
> repository are generated locally for educational purposes.

An automated Python ETL + reconciliation pipeline for a finance team that
receives **weekly Excel sales exports from multiple branches** and must verify
them against a **canonical database** (the official source for financial
reporting) before signing off.

The system answers one question:

> **"Does the Excel submission from every branch reconcile with the canonical
> database?"** — and if not, *exactly what is wrong and where*.

---

## 1. Project Overview

Manual weekly reconciliation (open Excel → eyeball rows → re-add totals →
compare with the database → email finance) is slow and dangerous: duplicates,
missing transactions, wrong types, blank values, bad totals, invalid branch
IDs and manual arithmetic errors all slip through — every single week.

This project replaces that with one command:

```bash
python run_pipeline.py
```

which ingests the workbook, validates it, loads only the valid rows into
SQLite **idempotently**, reconciles at three levels (global → branch →
transaction), and produces an `exception.xlsx` workbook, a
`validation_report.xlsx`, structured logs, and a unique Run ID for every
execution.

## 2. Architecture

```
                    ┌────────────────────┐
                    │  Branch Excel      │
                    │  Weekly Export     │
                    └─────────┬──────────┘
                              ▼
                    ┌────────────────────┐
                    │ Excel Ingestion    │   src/ingest.py (pandas/openpyxl)
                    └─────────┬──────────┘
                              ▼
                    ┌────────────────────┐
                    │ Schema Validation  │   src/validation.py
                    └─────────┬──────────┘   explicit SCHEMA_VALIDATION_FAILED
                              ▼
                    ┌────────────────────┐
                    │ Type / Null /      │
                    │ Duplicate / Branch │
                    │ Revenue checks     │
                    └─────────┬──────────┘
                     ┌────────┴────────┐
                     ▼                 ▼
              Valid Records       Invalid Records
                     │                 │
                     ▼                 ▼
        SQLite (processed_sales)   exception.xlsx
        UPSERT by transaction_id   (quarantined, never loaded)
                     │
                     ▼
        ┌────────────────────────────┐
        │ Reconciliation Engine      │  src/reconciliation.py
        │ L1 Global → L2 Branch →    │
        │ L3 Transaction             │
        └─────────┬──────────────────┘
                  ▼
   exception.xlsx · validation_report.xlsx · logs/pipeline.log · etl_runs
```

## 3. Dataset

* **Nature:** fully synthetic, generated locally (`generate_data.py`),
  labelled *Synthetic Dataset — Not Real Financial Data*.
* **Size:** 30,000 canonical rows → **30,030-row** branch submission workbook
  (`data/input/branch_sales.xlsx`, sheet `Branch_Sales`).
* **Columns:** `transaction_id` (str) · `branch_id` (str) ·
  `transaction_date` (date) · `customer_id` (str) · `product_id` (str) ·
  `quantity` (int) · `unit_price` (decimal) · `discount` (decimal) ·
  `revenue` (decimal).
* **Dimensions:** 10 branches, 3,000 customers, 500 products;
  dates 2026-01-01 → 2026-08-31.

### Revenue rule (business rule, section 12)

```
gross_amount = quantity × unit_price
revenue      = gross_amount − discount
```

Validated within a decimal tolerance of **0.05** (float-rounding guard).

### Intentionally injected defects

| Defect | Count | Error type raised |
|---|---|---|
| Duplicate transactions | 50 ids (100 rows flagged) | `DUPLICATE_TRANSACTION` |
| Missing critical values | 50 | `MISSING_TRANSACTION_ID`, `MISSING_BRANCH_ID`, `MISSING_PRODUCT_ID`, `MISSING_QUANTITY`, `MISSING_PRICE`, `MISSING_REVENUE` |
| Invalid numerics (`"ABC"`, `"N/A"`, …) | 25 | `INVALID_INTEGER_VALUE` / `INVALID_NUMERIC_VALUE` |
| Incorrect revenue (breaks the rule) | 25 | `REVENUE_MISMATCH` |
| Invalid branch (`BR9xx`) | 20 | `INVALID_BRANCH` |
| Transactions the branch "forgot" | 20 | `MISSING_FROM_EXCEL` (reconciliation) |

## 4. Database Schema (`sql/schema.sql`)

| Table | Purpose | Key |
|---|---|---|
| `branches` | Branch dimension | `branch_id` PK |
| `customers` | Customer dimension | `customer_id` PK |
| `products` | Product dimension | `product_id` PK |
| `canonical_sales` | **Official** finance source of truth | `transaction_id` PK, FK→branches/products |
| `processed_sales` | Validated Excel records (loaded layer) | `transaction_id` PK |
| `etl_runs` | One row per pipeline execution (run tracking) | `run_id` PK |
| `reconciliation_results` | Per-run global + branch reconciliation rows | (`run_id`,`level`,`branch_id`) PK |

Constraints: primary keys on all entities, `NOT NULL` on required measures,
`DEFAULT 0` on discount, foreign keys from `canonical_sales` to the
dimensions, and indexes on `branch_id` / `loaded_run_id` for the
reconciliation queries.

## 5. Validation Rules (`src/validation.py`)

Executed **before any database load** — bad architecture (load-then-validate)
is explicitly avoided.

1. **Schema** — required / missing / unexpected / misnamed columns.
   Failure raises `SCHEMA_VALIDATION_FAILED` naming every missing and
   unexpected column, and the pipeline *stops before the database load*.
2. **Types** — `quantity` → integer; `unit_price`/`discount`/`revenue` →
   numeric; `transaction_date` → date. Coercion failures are **recorded with
   the original value** (`Original Value: ABC, Column: quantity, Error:
   INVALID_NUMERIC_VALUE, Row: 1837`) — never silently coerced to NaN.
3. **Missing values** — nulls in the 7 critical fields, each categorised.
4. **Duplicates** — `transaction_id.duplicated(keep=False)` flags *every*
   occurrence of a duplicated id.
5. **Branch referential check** — `branch_id` must exist in the canonical
   `branches` table.
6. **Revenue rule** — `|reported − (quantity×unit_price − discount)| ≤ 0.05`.

Any row with **any** error is quarantined to the exception workbook; only
clean rows reach the database.

## 6. Reconciliation Rules (`src/reconciliation.py`)

Three levels — a grand total alone can hide one missing + one wrong
transaction, so totals are never trusted in isolation:

* **Level 1 — Global:** total rows, total quantity, total revenue.
* **Level 2 — Branch:** per-branch rows / quantity / revenue with a
  PASS/FAIL status per branch (outer join, so a branch missing on either
  side still appears).
* **Level 3 — Transaction:**
  * `MISSING_FROM_DATABASE` — in Excel, not in the DB;
  * `MISSING_FROM_EXCEL` — in the DB, absent from the submission;
  * `QUANTITY_MISMATCH` / `PRICE_MISMATCH` / `REVENUE_MISMATCH` — field-level
    differences with Excel value, DB value and the signed difference.

## 7. Exception Handling

Invalid records are **never** loaded. They are written to
`reports/exception.xlsx` with one worksheet per category:

```
Summary · Schema_Errors · Missing_Values · Duplicates · Invalid_Types ·
Revenue_Mismatches · Missing_Transactions · Extra_Transactions ·
Branch_Reconciliation
```

The **Summary** sheet carries run metadata and every headline metric
(input/valid/invalid/duplicate rows, branches passed/failed, transaction
mismatches, DQ score, overall status). PASS/FAIL cells are colour-coded.

## 8. Idempotency ⭐

**Approach: primary key + upsert.** `processed_sales.transaction_id` is a
PRIMARY KEY and loading uses SQLite's
`INSERT … ON CONFLICT(transaction_id) DO UPDATE` (in 90-row chunks to stay
under SQLite's bound-variable limit). Re-running the pipeline on the same
input **updates the same keys in place** instead of inserting again:

```
Run 1 → processed_sales = 29,816 rows
Run 2 → processed_sales = 29,816 rows   ✅ (not 59,632)
```

Additionally every run is upserted into `etl_runs` by `run_id`, and
`reconciliation_results` rows are replaced per run — so reports and run
history never duplicate either. Verified automatically by
`tests/test_idempotency.py`.

## 9. Testing (`pytest`, 20 tests)

| File | Covers |
|---|---|
| `tests/test_validation.py` | Missing column → explicit `SCHEMA_VALIDATION_FAILED`; unexpected columns; duplicate detection (keep=False); categorised missing values; invalid numerics **preserving original values**; invalid dates; revenue rule + tolerance; invalid branches; valid/invalid split |
| `tests/test_reconciliation.py` | `MISSING_FROM_DATABASE`, `MISSING_FROM_EXCEL`, transaction revenue mismatch, global totals, per-branch PASS/FAIL, identical data passes everywhere |
| `tests/test_idempotency.py` | **Mandatory:** run the ETL twice → `count_after_first_run == count_after_second_run`; end-to-end deliverables (reports, log, Run ID, required sheets) |

## 10. Execution

```bash
pip install -r requirements.txt     # pandas, openpyxl, sqlalchemy, pytest

python generate_data.py             # (re)generate the synthetic workbook
python run_pipeline.py              # run the reconciliation pipeline
python run_pipeline.py              # run again — row count stays identical
pytest                              # 20 automated tests
```

Optional PostgreSQL extension: `pip install psycopg2-binary` and point
`src/database.py::get_engine` at a `postgresql://` URL — the schema and
upsert logic are dialect-compatible.

## Latest run (actual output)

```
==================================================
AUTOMATED RECONCILIATION PIPELINE
==================================================

Run ID: RUN-20260908-155628-7C45

Input rows:                 30,030
Valid rows:                 29,816
Invalid rows:                  214
Duplicate rows:                100

Database rows:              29,816

Excel revenue:        177,261,928.03
Database revenue:     178,308,509.18

Revenue difference:    -1,046,581.15

Branches checked:               10
Branches passed:                 0
Branches failed:                10

Transaction mismatches:         184

Data Quality Score:    78.5 (Warning)

Overall Status:
REQUIRES_INVESTIGATION
==================================================
```

All 10 branches FAIL **correctly**: every branch is affected by the injected
defects (quarantined duplicates/missing/invalid rows reduce each branch's
valid row count, and 20 canonical transactions were removed from the
submission entirely). Among the 29,816 transactions present on **both**
sides there are **0 revenue and 0 quantity mismatches** — the engine detects
exactly the injected defects and nothing else.

## Advanced Extension — Option E: Data Quality Score

```
DQ Score = 100
  − 1.0 × duplicate rows        per 1,000 input rows
  − 1.5 × missing values        per 1,000 input rows
  − 2.0 × invalid types         per 1,000 input rows
  − 2.0 × revenue mismatches    per 1,000 input rows
  − 2.5 × invalid branches      per 1,000 input rows
  − 10.0 flat if any branch fails reconciliation

95–100 Excellent · 90–94 Good · 75–89 Warning · <75 Failed
```

**Justification:** penalties are normalised per 1,000 input rows so scores
are comparable across weekly files of different sizes; weights scale with
financial severity — referential violations (invalid branch) and
revenue-rule breaks are costlier than a duplicated id, and a failed
branch-level reconciliation is the strongest signal finance cares about, so
it carries a flat 10-point penalty. This submission scores **78.5 (Warning)**.

## Production considerations

* **Data-quality framework:** the validation layer maps naturally onto
  Great Expectations (`expect_column_values_to_not_be_null`,
  `expect_column_values_to_be_between` for quantity/price/revenue,
  `expect_column_values_to_be_in_set` for branch_id).
* **Scheduling:** run every Friday — receive branch files → automated ETL →
  validation → reconciliation → exception report → finance notification.
* **Database:** move from SQLite to PostgreSQL for production (constraints,
  indexes, transactions, upserts, migrations are already written in a
  dialect-compatible way).

## Project structure

```
Day-6-Excel-Database-Reconciliation/
├── README.md
├── generate_data.py          # synthetic data generator (with defects)
├── run_pipeline.py           # entry point
├── requirements.txt
├── pytest.ini
├── data/
│   ├── input/branch_sales.xlsx
│   └── canonical/{canonical_sales,branches,customers,products}.csv
├── database/reconciliation.db
├── src/
│   ├── config.py  exceptions.py  logging_utils.py
│   ├── ingest.py  validation.py  transform.py
│   ├── database.py  reconciliation.py  reporting.py  pipeline.py
├── sql/schema.sql
├── reports/{exception.xlsx, validation_report.xlsx}
├── logs/pipeline.log
└── tests/{test_validation.py, test_reconciliation.py, test_idempotency.py}
```
