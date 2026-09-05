


# Day 01 — Executive Sales Performance Diagnostic

## Project Overview
Revenue-quality diagnostic for an e-commerce business showing top-line growth
but weakening repeat purchasing. Built on the UCI Online Retail dataset
(541,909 transactions, Dec 2010 – Dec 2011).

## Business Problem
Leadership sees revenue growth but falling repeat purchases and needs the
operational drivers behind revenue, cancellations and customer-value changes.

## Objective
A decision-ready diagnostic — not a generic EDA — with reconciled KPIs and
five evidence-backed actions.

## Dataset
UCI Online Retail (#352). Fields: InvoiceNo, StockCode, Description, Quantity,
InvoiceDate, UnitPrice, CustomerID, Country.

## Data Dictionary
See notebook section 3 — business meaning, type, usage and quality issue per field.

## Business Rules
CANCELLATION = InvoiceNo prefix "C"; ADJUSTMENT = negative price / service
codes; INVALID = zero quantity or zero price; SALE = everything else.
Repeat customer = 2+ valid sale orders. Loyal = 4+.

## Data Cleaning
Exact duplicates removed (count logged); missing Description labelled;
missing CustomerID retained for revenue, excluded only from customer-level
analysis. No silent row deletion — full cleaning log exported.

## KPI Definitions
Gross = Σ signed revenue on SALE lines; Cancellation = |signed| on C-lines;
Net = Gross − Cancellation; AOV = Gross / distinct sale invoices (order grain);
Repeat rate = repeat customers / identified customers.

## Analytical Methodology
Transaction → order → customer → country/product/month aggregation, revenue
decomposition (Customers × Orders/Customer × AOV), cancellation profiling,
Pareto concentration, RFM overlay.

## Power BI Dashboard
5 pages (Executive, Customer & Retention, Product, Country, Revenue Quality);
star schema on 02_fact_orders + 01_fact_transactions; DAX measures in notebook §26.

## Key Findings / Recommendations
Generated programmatically from the data — see notebook §22–23 and
reports/executive_findings.txt.

## Validation
13 automated reconciliation checks (row counts, revenue identities, grain
checks) — all must PASS; report exported as 13_validation_report.csv.

## Production Considerations
Move KPI logic to a governed semantic layer (dbt/Power BI dataset), automate
the validation suite as pipeline tests, monitor unknown-CustomerID share.

## Technologies
Python, pandas, NumPy, Plotly, Jupyter/Colab, Power BI.

## Project Structure
See notebook §28.

## 30. requirements.txt

```
pandas>=2.0
numpy>=1.24
openpyxl>=3.1
plotly>=5.18
pyarrow>=14.0
jupyter>=1.0
```

---
### Production Considerations (as specified in the brief)
- **Governed semantic layer:** promote the KPI definitions in §17 to dbt models
  or a Power BI dataset so every consumer computes identically.
- **Automated KPI tests:** the §18 validation suite should run in CI on every
  data refresh, failing the publish on any FAIL.
- **Partial-period handling:** the final month (Dec 2011 = 9 days) must be
  excluded or annotated in any trend comparison.
- **Identity coverage:** track unknown-CustomerID revenue share as a data-quality
  KPI — it bounds the trustworthiness of every retention metric.

*End of notebook — every figure computed from the source data, nothing invented.*
