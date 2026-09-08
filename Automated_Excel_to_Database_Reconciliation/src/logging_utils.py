"""Structured logging with a unique Run ID attached to every record."""
import logging
import sys
import uuid
from datetime import datetime
from pathlib import Path


def generate_run_id(now: datetime | None = None) -> str:
    """RUN-YYYYMMDD-HHMMSS-XXXX (e.g. RUN-20260908-201530-A8F2)."""
    now = now or datetime.now()
    return f"RUN-{now:%Y%m%d-%H%M%S}-{uuid.uuid4().hex[:4].upper()}"


class RunIdFilter(logging.Filter):
    """Injects the current Run ID into every log record."""

    def __init__(self, run_id: str):
        super().__init__()
        self.run_id = run_id

    def filter(self, record: logging.LogRecord) -> bool:
        record.run_id = self.run_id
        return True


def get_logger(run_id: str, log_file: Path) -> logging.Logger:
    """Return a logger writing 'timestamp | LEVEL | RUN-ID | message' lines
    to both the console and logs/pipeline.log."""
    logger = logging.getLogger(f"recon.{run_id}")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    # Reset handlers so repeated runs (and tests) do not duplicate lines.
    logger.handlers.clear()

    fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(run_id)s | %(message)s")
    run_filter = RunIdFilter(run_id)

    log_file.parent.mkdir(parents=True, exist_ok=True)
    fh = logging.FileHandler(log_file, mode="a", encoding="utf-8")
    fh.setFormatter(fmt)
    fh.addFilter(run_filter)
    logger.addHandler(fh)

    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(fmt)
    sh.addFilter(run_filter)
    logger.addHandler(sh)
    return logger
