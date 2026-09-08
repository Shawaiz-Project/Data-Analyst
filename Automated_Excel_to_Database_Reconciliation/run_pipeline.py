#!/usr/bin/env python3
"""Entry point: python run_pipeline.py

Executes the automated Excel-to-database reconciliation pipeline and
prints the finance-facing summary (section 41).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from src.pipeline import run_pipeline  # noqa: E402


def main() -> int:
    result = run_pipeline()
    s = result.get("stats", {})

    print()
    print("=" * 50)
    print("AUTOMATED RECONCILIATION PIPELINE")
    print("=" * 50)
    print(f"\nRun ID: {result['run_id']}\n")

    if result["status"] == "SCHEMA_VALIDATION_FAILED":
        err = result["schema_error"]
        print("SCHEMA_VALIDATION_FAILED\n")
        if err["missing_columns"]:
            print("Missing columns:")
            for c in err["missing_columns"]:
                print(f"- {c}")
        if err["unexpected_columns"]:
            print("\nUnexpected columns:")
            for c in err["unexpected_columns"]:
                print(f"- {c}")
        print("\nPipeline stopped before database load.")
        return 2

    def row(label, value):
        print(f"{label:<22}{value:>12,}"
              if isinstance(value, (int, float)) else
              f"{label:<22}{value:>12}")

    row("Input rows:", s.get("input_rows", 0))
    row("Valid rows:", s.get("valid_rows", 0))
    row("Invalid rows:", s.get("invalid_rows", 0))
    row("Duplicate rows:", s.get("duplicate_rows", 0))
    print()
    row("Database rows:", s.get("database_rows", 0))
    print()
    row("Excel revenue:", round(s.get("excel_revenue", 0), 2))
    row("Database revenue:", round(s.get("db_revenue", 0), 2))
    print()
    row("Revenue difference:", round(s.get("revenue_difference", 0), 2))
    print()
    row("Branches checked:", s.get("branches_checked", 0))
    row("Branches passed:", s.get("branches_passed", 0))
    row("Branches failed:", s.get("branches_failed", 0))
    print()
    row("Transaction mismatches:", s.get("transaction_mismatches", 0))
    print(f"\nData Quality Score:    {s.get('dq_score')} ({s.get('dq_rating')})")
    print(f"\nOverall Status:\n{s.get('overall_status')}")
    print("\nException report:\nreports/exception.xlsx")
    print("\nValidation report:\nreports/validation_report.xlsx")
    print("=" * 50)
    return 0


if __name__ == "__main__":
    sys.exit(main())
