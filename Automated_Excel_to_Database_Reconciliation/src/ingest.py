"""Phase 2 — Excel ingestion.

Loads the branch sales workbook with pandas/openpyxl and records the
file name, worksheet name, row/column counts and timing for the run.
"""
import time
from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd

from . import config
from .exceptions import PipelineError


@dataclass
class IngestResult:
    df: pd.DataFrame
    file_name: str
    worksheet: str
    n_rows: int
    n_cols: int
    start_time: float = field(default=0.0)
    end_time: float = field(default=0.0)

    @property
    def elapsed_seconds(self) -> float:
        return round(self.end_time - self.start_time, 3)


def load_excel(excel_path: Path | None = None,
               sheet_name: str | None = None,
               logger=None) -> IngestResult:
    """Read the branch Excel workbook. All columns are read as-is (dtype
    preserved) so type validation later sees the *original* values."""
    excel_path = Path(excel_path or config.EXCEL_FILE)
    sheet_name = sheet_name or config.EXCEL_SHEET

    if not excel_path.exists():
        raise PipelineError(f"Input file not found: {excel_path}")

    start = time.time()
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    end = time.time()

    result = IngestResult(
        df=df,
        file_name=excel_path.name,
        worksheet=sheet_name,
        n_rows=len(df),
        n_cols=len(df.columns),
        start_time=start,
        end_time=end,
    )
    if logger:
        logger.info("Excel loaded | file=%s sheet=%s rows=%d cols=%d",
                    result.file_name, result.worksheet, result.n_rows, result.n_cols)
    return result
