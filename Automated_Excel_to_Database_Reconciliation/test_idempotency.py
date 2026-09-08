"""Mandatory idempotency test (section 35) + end-to-end pipeline test.

Runs the full pipeline TWICE against a temporary database and asserts:
    count_after_first_run == count_after_second_run
"""
import shutil
from pathlib import Path

import pandas as pd
import pytest

from src import config, database
from src.pipeline import run_pipeline

PROJECT_ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture()
def workspace(tmp_path):
    """Isolated tmp workspace reusing the project's real input data."""
    (tmp_path / "reports").mkdir()
    (tmp_path / "logs").mkdir()
    return tmp_path


def test_pipeline_is_idempotent(workspace):
    db_path = workspace / "recon.db"
    kwargs = dict(excel_path=config.EXCEL_FILE,
                  db_path=db_path,
                  reports_dir=workspace / "reports",
                  logs_dir=workspace / "logs",
                  canonical_dir=config.DATA_CANONICAL_DIR)

    r1 = run_pipeline(run_id="RUN-TEST-IDEMPOTENT-0001", **kwargs)
    engine = database.get_engine(db_path)
    count_first = database.table_count(engine, "processed_sales")

    r2 = run_pipeline(run_id="RUN-TEST-IDEMPOTENT-0002", **kwargs)
    count_second = database.table_count(engine, "processed_sales")

    assert count_first > 0
    assert count_first == count_second           # <-- the mandatory assertion
    assert r1["stats"]["valid_rows"] == r2["stats"]["valid_rows"]
    assert count_second == r1["stats"]["valid_rows"]

    # both runs were tracked in etl_runs
    runs = database.fetch_table(engine, "etl_runs")
    assert set(runs["run_id"]) == {"RUN-TEST-IDEMPOTENT-0001",
                                   "RUN-TEST-IDEMPOTENT-0002"}


def test_pipeline_end_to_end_outputs(workspace):
    db_path = workspace / "recon2.db"
    result = run_pipeline(excel_path=config.EXCEL_FILE,
                          db_path=db_path,
                          reports_dir=workspace / "reports",
                          logs_dir=workspace / "logs",
                          canonical_dir=config.DATA_CANONICAL_DIR,
                          run_id="RUN-TEST-E2E-0001")
    assert result["status"] in ("READY_FOR_FINANCE_SIGNOFF",
                                "REQUIRES_INVESTIGATION")
    # mandatory deliverables produced
    assert (workspace / "reports" / "exception.xlsx").exists()
    assert (workspace / "reports" / "validation_report.xlsx").exists()
    assert (workspace / "logs" / "pipeline.log").exists()
    # log carries the run id
    assert "RUN-TEST-E2E-0001" in (workspace / "logs" / "pipeline.log").read_text()
    # exception workbook has the required sheets
    sheets = pd.ExcelFile(workspace / "reports" / "exception.xlsx").sheet_names
    for required in ["Summary", "Schema_Errors", "Missing_Values", "Duplicates",
                     "Invalid_Types", "Revenue_Mismatches",
                     "Missing_Transactions", "Extra_Transactions",
                     "Branch_Reconciliation"]:
        assert required in sheets
