"""Central configuration for the reconciliation pipeline."""
from pathlib import Path

# --- Project paths -----------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_INPUT_DIR = PROJECT_ROOT / "data" / "input"
DATA_CANONICAL_DIR = PROJECT_ROOT / "data" / "canonical"
DATABASE_DIR = PROJECT_ROOT / "database"
DB_PATH = DATABASE_DIR / "reconciliation.db"
REPORTS_DIR = PROJECT_ROOT / "reports"
LOGS_DIR = PROJECT_ROOT / "logs"
SQL_SCHEMA_FILE = PROJECT_ROOT / "sql" / "schema.sql"

EXCEL_FILE = DATA_INPUT_DIR / "branch_sales.xlsx"
EXCEL_SHEET = "Branch_Sales"

CANONICAL_SALES_CSV = DATA_CANONICAL_DIR / "canonical_sales.csv"
BRANCHES_CSV = DATA_CANONICAL_DIR / "branches.csv"
CUSTOMERS_CSV = DATA_CANONICAL_DIR / "customers.csv"
PRODUCTS_CSV = DATA_CANONICAL_DIR / "products.csv"

# --- Schema -------------------------------------------------------------------
EXPECTED_COLUMNS = [
    "transaction_id", "branch_id", "transaction_date", "customer_id",
    "product_id", "quantity", "unit_price", "discount", "revenue",
]

ID_COLUMNS = ["transaction_id", "branch_id", "customer_id", "product_id"]
NUMERIC_COLUMNS = ["unit_price", "discount", "revenue"]
INTEGER_COLUMNS = ["quantity"]
DATE_COLUMNS = ["transaction_date"]

# Revenue business rule:  revenue = quantity * unit_price - discount
REVENUE_TOLERANCE = 0.05  # decimal tolerance for float rounding

# Critical fields for missing-value validation (field -> error type)
CRITICAL_FIELDS = {
    "transaction_id": "MISSING_TRANSACTION_ID",
    "branch_id": "MISSING_BRANCH_ID",
    "transaction_date": "MISSING_TRANSACTION_DATE",
    "product_id": "MISSING_PRODUCT_ID",
    "quantity": "MISSING_QUANTITY",
    "unit_price": "MISSING_PRICE",
    "revenue": "MISSING_REVENUE",
}

# --- Data Quality Score penalties (Advanced Extension — Option E) -------------
# score = 100 - penalties (per 1,000 input rows), reconciliation penalty if any
# branch fails. Justification documented in README.md.
DQ_PENALTY_PER_1000 = {
    "DUPLICATE_TRANSACTION": 1.0,
    "MISSING_VALUE": 1.5,
    "INVALID_TYPE": 2.0,
    "REVENUE_MISMATCH": 2.0,
    "INVALID_BRANCH": 2.5,
}
DQ_RECONCILIATION_PENALTY = 10.0  # applied once when any branch fails
