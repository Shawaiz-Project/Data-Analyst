"""Phase 7–8 — database layer (SQLAlchemy, SQLite by default).

Key design points:
* schema.sql is the single source of truth for the DDL;
* processed_sales.transaction_id is a PRIMARY KEY and loading uses an
  INSERT ... ON CONFLICT DO UPDATE (upsert) so re-running the pipeline
  on the same input NEVER duplicates rows (idempotency — section 33);
* every run is recorded in etl_runs (section 21).
"""
from __future__ import annotations

from datetime import datetime
from pathlib import Path

import pandas as pd
from sqlalchemy import (Column, Date, DateTime, Float, Integer, MetaData,
                        String, Table, Text, create_engine, func, select)
from sqlalchemy.dialects.sqlite import insert as sqlite_insert

from . import config

_METADATA = MetaData()

processed_sales = Table(
    "processed_sales", _METADATA,
    Column("transaction_id", Text, primary_key=True),
    Column("branch_id", Text, nullable=False),
    Column("transaction_date", Date, nullable=False),
    Column("customer_id", Text),
    Column("product_id", Text, nullable=False),
    Column("quantity", Integer, nullable=False),
    Column("unit_price", Float, nullable=False),
    Column("discount", Float),
    Column("revenue", Float, nullable=False),
    Column("loaded_run_id", Text),
)

etl_runs = Table(
    "etl_runs", _METADATA,
    Column("run_id", Text, primary_key=True),
    Column("started_at", DateTime),
    Column("completed_at", DateTime),
    Column("input_file", Text),
    Column("worksheet", Text),
    Column("input_rows", Integer),
    Column("valid_rows", Integer),
    Column("invalid_rows", Integer),
    Column("duplicate_rows", Integer),
    Column("dq_score", Float),
    Column("status", String),
)

reconciliation_results = Table(
    "reconciliation_results", _METADATA,
    Column("run_id", Text, primary_key=True),
    Column("level", String, primary_key=True),
    Column("branch_id", Text, primary_key=True),
    Column("excel_rows", Integer),
    Column("db_rows", Integer),
    Column("row_diff", Integer),
    Column("excel_quantity", Float),
    Column("db_quantity", Float),
    Column("quantity_diff", Float),
    Column("excel_revenue", Float),
    Column("db_revenue", Float),
    Column("revenue_diff", Float),
    Column("status", String),
)

SALES_COLUMNS = ["transaction_id", "branch_id", "transaction_date",
                 "customer_id", "product_id", "quantity", "unit_price",
                 "discount", "revenue"]


def get_engine(db_path: Path | str | None = None):
    db_path = Path(db_path or config.DB_PATH)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    return create_engine(f"sqlite:///{db_path}")


def create_schema(engine, schema_file: Path | str | None = None) -> None:
    """Execute sql/schema.sql against the database."""
    schema_file = Path(schema_file or config.SQL_SCHEMA_FILE)
    ddl = schema_file.read_text(encoding="utf-8")
    with engine.begin() as conn:
        for statement in ddl.split(";"):
            stmt = statement.strip()
            if stmt:
                conn.exec_driver_sql(stmt)


def load_dimensions(engine, canonical_dir: Path | None = None, logger=None) -> list[str]:
    """Load branches / customers / products dimension CSVs and return the
    list of valid branch ids."""
    canonical_dir = Path(canonical_dir or config.DATA_CANONICAL_DIR)
    for name, csv in [("branches", "branches.csv"),
                      ("customers", "customers.csv"),
                      ("products", "products.csv")]:
        df = pd.read_csv(canonical_dir / csv)
        df.to_sql(name, engine, if_exists="replace", index=False)
    with engine.connect() as conn:
        branch_ids = [r[0] for r in conn.execute(select(Table(
            "branches", _METADATA, autoload_with=engine).c.branch_id))]
    if logger:
        logger.info("Dimensions loaded | branches=%d", len(branch_ids))
    return branch_ids


def load_canonical_sales(engine, csv_path: Path | None = None, logger=None) -> int:
    """Load the canonical (official) sales — the finance source of truth."""
    csv_path = Path(csv_path or config.CANONICAL_SALES_CSV)
    df = pd.read_csv(csv_path, parse_dates=["transaction_date"])
    df["transaction_date"] = pd.to_datetime(df["transaction_date"]).dt.date
    df.to_sql("canonical_sales", engine, if_exists="replace", index=False)
    if logger:
        logger.info("Canonical sales loaded | rows=%d", len(df))
    return len(df)


def upsert_processed_sales(engine, load_df: pd.DataFrame, run_id: str,
                           logger=None) -> int:
    """Idempotent load: INSERT ... ON CONFLICT(transaction_id) DO UPDATE.

    Run 1 inserts N rows; Run 2 on the same input updates the same N
    primary keys in place, so the table never grows to 2N."""
    if load_df.empty:
        return 0
    records = load_df.to_dict(orient="records")
    # SQLite caps bound variables per statement (999 in older builds), so
    # the upsert runs in chunks of 90 rows (10 columns -> 900 variables).
    chunk_size = 90
    with engine.begin() as conn:
        for start in range(0, len(records), chunk_size):
            chunk = records[start:start + chunk_size]
            stmt = sqlite_insert(processed_sales).values(chunk)
            update_cols = {c.name: stmt.excluded[c.name]
                           for c in processed_sales.columns
                           if c.name != "transaction_id"}
            stmt = stmt.on_conflict_do_update(
                index_elements=["transaction_id"], set_=update_cols)
            conn.execute(stmt)
    if logger:
        logger.info("Database load completed (upsert) | rows=%d", len(records))
    return len(records)


def fetch_table(engine, table_name: str) -> pd.DataFrame:
    with engine.connect() as conn:
        return pd.read_sql_table(table_name, conn)


def table_count(engine, table_name: str) -> int:
    tbl = Table(table_name, _METADATA, autoload_with=engine)
    with engine.connect() as conn:
        return int(conn.execute(select(func.count()).select_from(tbl)).scalar())


def record_run(engine, run_id: str, started_at: datetime, **fields) -> None:
    """Insert or update one etl_runs row for this execution."""
    row = {"run_id": run_id, "started_at": started_at, **fields}
    with engine.begin() as conn:
        stmt = sqlite_insert(etl_runs).values(row)
        update_cols = {k: v for k, v in row.items() if k != "run_id"}
        stmt = stmt.on_conflict_do_update(
            index_elements=["run_id"], set_=update_cols)
        conn.execute(stmt)


def save_reconciliation_results(engine, results_df: pd.DataFrame,
                                run_id: str) -> None:
    """Replace this run's reconciliation rows (idempotent per run)."""
    df = results_df.copy()
    df.insert(0, "run_id", run_id)
    with engine.begin() as conn:
        conn.execute(reconciliation_results.delete()
                     .where(reconciliation_results.c.run_id == run_id))
        df.to_sql("reconciliation_results", conn,
                  if_exists="append", index=False)
