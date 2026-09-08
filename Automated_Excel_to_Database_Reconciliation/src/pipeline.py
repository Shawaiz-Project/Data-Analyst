"""Pipeline orchestration — wires every phase together end to end.

Flow:  ingest -> schema validation -> type/null/duplicate/branch/revenue
       validation -> split valid/invalid -> idempotent DB load ->
       3-level reconciliation -> reports -> etl_runs record.
"""
from __future__ import annotations

from datetime import datetime
from pathlib import Path

from . import config, database, reporting, reconciliation, transform, validation
from .exceptions import SchemaValidationError
from .ingest import load_excel
from .logging_utils import generate_run_id, get_logger


def run_pipeline(excel_path: Path | None = None,
                 db_path: Path | None = None,
                 reports_dir: Path | None = None,
                 logs_dir: Path | None = None,
                 canonical_dir: Path | None = None,
                 run_id: str | None = None) -> dict:
    """Execute the full reconciliation pipeline. Returns a result dict."""
    run_id = run_id or generate_run_id()
    logs_dir = Path(logs_dir or config.LOGS_DIR)
    reports_dir = Path(reports_dir or config.REPORTS_DIR)
    logger = get_logger(run_id, logs_dir / "pipeline.log")
    started_at = datetime.now()

    logger.info("Pipeline started")
    result = {"run_id": run_id, "status": "FAILED"}

    engine = database.get_engine(db_path)
    database.create_schema(engine)

    # ------------------------------------------------------------------
    # Phase 2 — Ingestion
    # ------------------------------------------------------------------
    ingested = load_excel(excel_path, logger=logger)

    # ------------------------------------------------------------------
    # Phase 3 — Schema validation (explicit failure, stop before DB load)
    # ------------------------------------------------------------------
    schema_error = None
    try:
        schema_status = validation.validate_schema(ingested.df, logger=logger)
    except SchemaValidationError as exc:
        schema_error = {"missing_columns": exc.missing_columns,
                        "unexpected_columns": exc.unexpected_columns}
        stats = {"input_rows": ingested.n_rows,
                 "overall_status": "REQUIRES_INVESTIGATION"}
        reporting.write_exception_workbook(
            reports_dir / "exception.xlsx", run_id, stats,
            exceptions_df=None or __import__("pandas").DataFrame(),
            branch_recon_df=__import__("pandas").DataFrame(),
            txn_mismatch_df=__import__("pandas").DataFrame(),
            schema_error=schema_error, logger=logger)
        reporting.write_validation_report(
            reports_dir / "validation_report.xlsx", run_id,
            [("Schema Validation", "FAIL", str(exc).replace("\n", " | ")),
             ("Pipeline", "FAIL", "Stopped before database load")],
            stats, logger=logger)
        database.record_run(engine, run_id, started_at,
                            completed_at=datetime.now(),
                            input_file=ingested.file_name,
                            worksheet=ingested.worksheet,
                            input_rows=ingested.n_rows,
                            status="SCHEMA_VALIDATION_FAILED")
        logger.error("status=SCHEMA_VALIDATION_FAILED")
        result.update({"status": "SCHEMA_VALIDATION_FAILED",
                       "schema_error": schema_error, "stats": stats})
        return result

    # ------------------------------------------------------------------
    # Dimensions + canonical data (official source of truth)
    # ------------------------------------------------------------------
    valid_branch_ids = database.load_dimensions(engine, canonical_dir, logger=logger)
    canonical_dir = Path(canonical_dir or config.DATA_CANONICAL_DIR)
    database.load_canonical_sales(
        engine, canonical_dir / "canonical_sales.csv", logger=logger)

    # ------------------------------------------------------------------
    # Phases 4–6 — data-quality validation, split valid / invalid
    # ------------------------------------------------------------------
    valid_df, invalid_df, exceptions_df, stats = validation.run_all_validations(
        ingested.df, valid_branch_ids, logger=logger)
    logger.info("Validation split | valid=%d invalid=%d",
                stats["valid_rows"], stats["invalid_rows"])

    # ------------------------------------------------------------------
    # Phase 8 — idempotent load of valid records
    # ------------------------------------------------------------------
    load_df = transform.to_load_frame(valid_df, run_id=run_id)
    database.upsert_processed_sales(engine, load_df, run_id, logger=logger)
    db_rows_total = database.table_count(engine, "processed_sales")
    logger.info("processed_sales total rows after load = %d", db_rows_total)

    # ------------------------------------------------------------------
    # Phase 9 — three-level reconciliation vs canonical DB
    # ------------------------------------------------------------------
    db_df = database.fetch_table(engine, "canonical_sales")
    # Reconcile against the CURRENT submission's valid records (the
    # "Excel side" of the reconciliation), keeping dtype parity with DB.
    excel_side = transform.to_load_frame(valid_df)
    global_row, branch_df, txn_df, recon_summary = reconciliation.run_reconciliation(
        excel_side, db_df, logger=logger)

    stats.update(recon_summary)
    stats["database_rows"] = db_rows_total
    stats["excel_revenue"] = global_row["excel_revenue"]
    stats["db_revenue"] = global_row["db_revenue"]
    stats["revenue_difference"] = global_row["revenue_diff"]

    # ------------------------------------------------------------------
    # Overall status + Data Quality Score (Advanced Extension E)
    # ------------------------------------------------------------------
    dq_score, dq_rating = reporting.compute_dq_score(stats)
    stats["dq_score"] = dq_score
    stats["dq_rating"] = dq_rating

    all_pass = (global_row["status"] == "PASS"
                and recon_summary["branches_failed"] == 0
                and stats["invalid_rows"] == 0)
    overall = "READY_FOR_FINANCE_SIGNOFF" if all_pass else "REQUIRES_INVESTIGATION"
    stats["overall_status"] = overall

    # ------------------------------------------------------------------
    # Reports + run tracking
    # ------------------------------------------------------------------
    reporting.write_exception_workbook(
        reports_dir / "exception.xlsx", run_id, stats,
        exceptions_df=exceptions_df, branch_recon_df=branch_df,
        txn_mismatch_df=txn_df, logger=logger)

    stage_statuses = [
        ("Schema Validation", "PASS", "All required columns present"),
        ("Data Quality",
         "PASS" if stats["invalid_rows"] == 0 else "FAIL",
         f"invalid_rows={stats['invalid_rows']} "
         f"(duplicates={stats['duplicate_rows']}, "
         f"missing={stats['missing_values']}, "
         f"invalid_types={stats['invalid_types']}, "
         f"invalid_branches={stats['invalid_branches']}, "
         f"revenue_mismatches={stats['revenue_mismatches']})"),
        ("Database Load", "PASS",
         f"upserted={stats['valid_rows']} total_rows={db_rows_total}"),
        ("Reconciliation",
         "PASS" if recon_summary["branches_failed"] == 0 else "FAIL",
         f"branches_failed={recon_summary['branches_failed']} "
         f"txn_mismatches={recon_summary['transaction_mismatches']}"),
        ("Data Quality Score", f"{dq_score} ({dq_rating})",
         "100 - weighted defect penalties - reconciliation penalty"),
        ("Overall", overall, f"run_id={run_id}"),
    ]
    reporting.write_validation_report(
        reports_dir / "validation_report.xlsx", run_id,
        stage_statuses, stats, logger=logger)

    recon_full = __import__("pandas").concat(
        [__import__("pandas").DataFrame([global_row]), branch_df],
        ignore_index=True)
    database.save_reconciliation_results(engine, recon_full, run_id)
    database.record_run(engine, run_id, started_at,
                        completed_at=datetime.now(),
                        input_file=ingested.file_name,
                        worksheet=ingested.worksheet,
                        input_rows=stats["input_rows"],
                        valid_rows=stats["valid_rows"],
                        invalid_rows=stats["invalid_rows"],
                        duplicate_rows=stats["duplicate_rows"],
                        dq_score=dq_score, status=overall)

    logger.info("status=%s", overall)
    logger.info("Pipeline finished")

    result.update({"status": overall, "stats": stats,
                   "schema_status": schema_status,
                   "exceptions": exceptions_df,
                   "branch_reconciliation": branch_df,
                   "transaction_mismatches": txn_df,
                   "global_reconciliation": global_row})
    return result
