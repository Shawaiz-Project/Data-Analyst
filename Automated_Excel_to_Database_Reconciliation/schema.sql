-- =====================================================================
-- Day 6 — Automated Excel-to-Database Reconciliation
-- Database schema (SQLite / PostgreSQL compatible)
-- Synthetic Dataset — Not Real Financial Data
-- =====================================================================

-- Dimension: branches -------------------------------------------------
CREATE TABLE IF NOT EXISTS branches (
    branch_id   TEXT PRIMARY KEY,
    branch_name TEXT NOT NULL
);

-- Dimension: customers ------------------------------------------------
CREATE TABLE IF NOT EXISTS customers (
    customer_id   TEXT PRIMARY KEY,
    customer_name TEXT
);

-- Dimension: products -------------------------------------------------
CREATE TABLE IF NOT EXISTS products (
    product_id   TEXT PRIMARY KEY,
    product_name TEXT,
    category     TEXT
);

-- Canonical (official) sales — the finance source of truth ------------
CREATE TABLE IF NOT EXISTS canonical_sales (
    transaction_id   TEXT PRIMARY KEY,
    branch_id        TEXT    NOT NULL REFERENCES branches(branch_id),
    transaction_date DATE    NOT NULL,
    customer_id      TEXT,
    product_id       TEXT    NOT NULL REFERENCES products(product_id),
    quantity         INTEGER NOT NULL,
    unit_price       NUMERIC NOT NULL,
    discount         NUMERIC DEFAULT 0,
    revenue          NUMERIC NOT NULL
);

-- Processed sales — validated records loaded from the branch Excel ----
-- PRIMARY KEY on transaction_id is what makes re-runs idempotent:
-- a second run UPSERTs the same keys instead of inserting duplicates.
CREATE TABLE IF NOT EXISTS processed_sales (
    transaction_id   TEXT PRIMARY KEY,
    branch_id        TEXT    NOT NULL,
    transaction_date DATE    NOT NULL,
    customer_id      TEXT,
    product_id       TEXT    NOT NULL,
    quantity         INTEGER NOT NULL,
    unit_price       NUMERIC NOT NULL,
    discount         NUMERIC DEFAULT 0,
    revenue          NUMERIC NOT NULL,
    loaded_run_id    TEXT
);

-- ETL run tracking — one row per pipeline execution -------------------
CREATE TABLE IF NOT EXISTS etl_runs (
    run_id          TEXT PRIMARY KEY,
    started_at      TIMESTAMP,
    completed_at    TIMESTAMP,
    input_file      TEXT,
    worksheet       TEXT,
    input_rows      INTEGER,
    valid_rows      INTEGER,
    invalid_rows    INTEGER,
    duplicate_rows  INTEGER,
    dq_score        NUMERIC,
    status          TEXT
);

-- Reconciliation results — one row per run per branch ------------------
CREATE TABLE IF NOT EXISTS reconciliation_results (
    run_id          TEXT NOT NULL,
    level           TEXT NOT NULL,          -- GLOBAL | BRANCH
    branch_id       TEXT NOT NULL,          -- '__ALL__' for the GLOBAL row
    excel_rows      INTEGER,
    db_rows         INTEGER,
    row_diff        INTEGER,
    excel_quantity  NUMERIC,
    db_quantity     NUMERIC,
    quantity_diff   NUMERIC,
    excel_revenue   NUMERIC,
    db_revenue      NUMERIC,
    revenue_diff    NUMERIC,
    status          TEXT,                   -- PASS | FAIL
    PRIMARY KEY (run_id, level, branch_id)
);

-- Helpful indexes for reconciliation queries ---------------------------
CREATE INDEX IF NOT EXISTS idx_processed_branch   ON processed_sales(branch_id);
CREATE INDEX IF NOT EXISTS idx_canonical_branch   ON canonical_sales(branch_id);
CREATE INDEX IF NOT EXISTS idx_processed_run      ON processed_sales(loaded_run_id);
