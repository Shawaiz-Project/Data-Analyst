"""Custom exceptions with explicit, non-silent failure semantics."""


class SchemaValidationError(Exception):
    """Raised when the Excel schema fails validation.

    The message is deliberately explicit: it names every missing and
    unexpected column and states that the pipeline stopped before the
    database load (assignment section 15).
    """

    def __init__(self, missing_columns, unexpected_columns):
        self.missing_columns = list(missing_columns)
        self.unexpected_columns = list(unexpected_columns)
        lines = ["SCHEMA_VALIDATION_FAILED", ""]
        if self.missing_columns:
            lines.append("Missing columns:")
            lines.extend(f"- {c}" for c in self.missing_columns)
        if self.unexpected_columns:
            lines.append("Unexpected columns:")
            lines.extend(f"- {c}" for c in self.unexpected_columns)
        lines.append("")
        lines.append("Pipeline stopped before database load.")
        super().__init__("\n".join(lines))


class PipelineError(Exception):
    """Generic fatal pipeline error (e.g. missing input file)."""
