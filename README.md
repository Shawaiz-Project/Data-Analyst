# 100 Days of Professional Data Scientist + AI/ML Engineer

## Program design  

This is a 100‑day professional‑work simulation. Each day is exactly one coherent assignment designed for approximately 2–5 hours, with capstones allowed to run longer. The progression follows the requested phases: professional analytics → data engineering → ML → production ML/MLOps → deep learning → GenAI → RAG → enterprise AI/research. The objective is to produce artifacts, diagnose failures, defend engineering decisions, and build a portfolio rather than complete tutorial exercises.

## Operating rules

- Use a feature branch for each meaningful task and open a pull request at milestones.
- Keep data, code, experiments, and reports versioned; never commit credentials.
- For research days, record exact paper/dataset/model versions, baseline, experiment, results, error analysis, limitations, and reproducibility details.
- Never fabricate dataset links, papers, results, or performance. Synthetic datasets must be labeled as synthetic.
- Suggested work cadence: Day task → artifact → tests → README update → commit → short reflection.

## Skill Map

| Skill | Days | Difficulty |
|-------|------|------------|
| Data Analytics | 1–20 | Advanced → Professional |
| SQL / Databases | 3,11–20,46,50,90–100 | Advanced → Expert |
| Data Engineering | 6,11–20,45,50,91,97,100 | Advanced → Production |
| Machine Learning | 9,21–50,92,96,100 | Advanced → Production |
| Deep Learning | 51–65,96,100 | Advanced → Systems |
| NLP | 56–62,66–80,100 | Advanced → Production |
| Generative AI | 66–80,90–100 | Advanced → Production |
| RAG | 69,81–90,92,98–100 | Advanced → Enterprise |
| MLOps | 15,18,38–50,78,90–100 | Advanced → Production |
| DevOps / Cloud | 40–50,78,91,93–95,100 | Intermediate → Production |
| Research | 26,33,44,57,58,62,70,76,84,89,92,96,99 | Advanced → Research |
| Security / Reliability | 42,67–80,88,94–95,97,100 | Advanced → Enterprise |

## Verified Dataset Registry

Use the registry ID in daily assignments. The registry centralizes the required source, approximate scale, task type, target, and known challenges. Public dataset details were checked against the listed source pages; exact revisions should be recorded when downloaded.

| ID | Dataset | Source URL | Approx. size / format | Task | Target | Major challenges |
|----|---------|------------|----------------------|------|--------|------------------|
| DR01 | UCI Online Retail | https://archive.ics.uci.edu/dataset/352/online-retail | 541,909 rows; 8 columns | transactions; customer/product/time analysis | CustomerID/InvoiceNo | cancellations, missing CustomerID, wholesale behavior |
| DR02 | UCI Bank Marketing | https://archive.ics.uci.edu/dataset/222/bank+marketing | 45,211 rows; 17 variables | binary classification | y | campaign imbalance, categorical handling, temporal ordering |
| DR03 | UCI Wine Quality | https://archive.ics.uci.edu/dataset/186/wine+quality | 4,898 combined red/white samples | classification/regression | quality | ordinal target, class imbalance, correlated features |
| DR04 | NYC TLC Trip Record Data | https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page | monthly taxi trip data; parquet/CSV | analytics/time series/fraud/anomaly | fare_amount, trip metrics | large volume, missing/invalid trips, changing schemas |
| DR05 | UCI Adult | https://archive.ics.uci.edu/dataset/2/adult | 48,842 rows; 14 predictors | classification/fairness | income | missing values, sensitive attributes, group disparities |
| DR06 | UCI Student Performance | https://archive.ics.uci.edu/dataset/320/student+performance | 649 rows; up to 33 variables | education analytics/regression/classification | G3 / performance | small sample, leakage from later-term variables |
| DR07 | UCI Predict Students' Dropout and Academic Success | https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success | 4,424 rows; 36 predictors | multiclass classification | target | class imbalance, temporal/academic leakage |
| DR08 | Hugging Face Banking77 | https://huggingface.co/datasets/mteb/banking77 | 13,083 utterances; 77 intents | intent classification/embeddings | label | fine-grained intent confusion |
| DR09 | Hugging Face CoNLL-2003 | https://huggingface.co/datasets/tner/conll2003 | 14,041 train / 3,250 validation / 3,453 test | named entity recognition | BIO entity tags | token alignment, domain shift |
| DR10 | Hugging Face GLUE/SST-2 | https://huggingface.co/datasets/nyu-mll/glue | sentiment classification benchmark | NLP classification | label | short text, sentiment ambiguity |
| DR11 | MNIST | https://yann.lecun.org/exdb/mnist/index.html | 60,000 train / 10,000 test 28×28 images | computer vision classification | digit | simple benchmark; avoid overfitting to benchmark habits |
| DR12 | MIMIC-IV Clinical Database Demo v2.2 | https://physionet.org/content/mimic-iv-demo/2.2/ | 15.5 MB demo release | clinical analytics | task-dependent | access/ethics, de-identification, clinical leakage |
| DR13 | MS MARCO | https://microsoft.github.io/msmarco/ | large-scale search/QA collection | retrieval/reranking/QA research | relevance | licensing, scale, retrieval evaluation |
| DR14 | Synthetic E-commerce Events | synthetic | generated locally; target 1–5M events | analytics/ETL/load testing | event_type / revenue | schema evolution, duplicates, late events |
| DR15 | Synthetic Support Tickets | synthetic | generated locally; target 100k–500k tickets | NLP/RAG/agent evaluation | intent/severity | PII simulation, adversarial prompts, ambiguous tickets |
| DR16 | Synthetic IoT Sensor Stream | synthetic | generated locally; target 10M+ observations | time-series/anomaly/MLOps | fault | drift, missing telemetry, sensor noise |

## Phase Map

- **Phase 1** — Days 1–10: Professional Data Analytics Foundations  
- **Phase 2** — Days 11–20: Advanced Analytics + Data Engineering  
- **Phase 3** — Days 21–35: Machine Learning  
- **Phase 4** — Days 36–50: Advanced ML + End-to-End ML Systems  
- **Phase 5** — Days 51–65: Deep Learning  
- **Phase 6** — Days 66–80: Generative AI + LLM Engineering  
- **Phase 7** — Days 81–90: RAG + Agentic AI  
- **Phase 8** — Days 91–100: Production AI + Research + MLOps  

## Daily Program

### Day 1 — Executive Sales Performance Diagnostic

**Role**  
Data Analyst

**Business/Technical Scenario**  
An e-commerce leadership team sees revenue growth but falling repeat purchases.

**Problem Statement**  
Find the operational drivers behind revenue, cancellations, and customer-value changes.

**Objective**  
Deliver a decision-ready diagnostic, not a generic EDA.

**Dataset / Data Source**  
DR01 — UCI Online Retail; ~541,909 transactions; Excel/Python import; key fields: InvoiceNo, StockCode, Quantity, InvoiceDate, UnitPrice, CustomerID, Country.

**Task**  
Build a revenue-quality diagnostic: clean transactions, define business rules for cancellations, calculate revenue/AOV/repeat-rate proxies, segment by country/product/customer, and write 5 evidence-backed actions.

**Technologies**  
Excel + Python + pandas + NumPy + Plotly

**Required Deliverables**  
Cleaned CSV/Parquet; analysis notebook; KPI table; executive dashboard; one-page decision memo.

**Acceptance Criteria**  
All KPI definitions documented; negative/cancelled transactions treated explicitly; totals reconcile to source; every recommendation cites a metric.

**Professional Skills Tested**  
Business KPI design, cleaning, aggregation, stakeholder communication

**Common Failure Modes**  
Treating cancelled invoices as ordinary sales; silently dropping missing CustomerID; mixing gross and net revenue.

**Production Considerations**  
Use a governed semantic layer and automated KPI tests before publishing.

**Extension Challenge**  
Add cohort-based repeat-purchase analysis by acquisition month.

**Git Commit**  
`feat(analytics): build ecommerce revenue diagnostic`

**Portfolio Value**  
Strong portfolio piece showing business thinking plus technical analytics; include dashboard screenshots and KPI definitions.

---

### Day 2 — Cohort Retention and Customer Value Analysis

**Role**  
Data Analyst

**Business/Technical Scenario**  
Marketing wants to know whether new customers become durable revenue contributors.

**Problem Statement**  
Construct acquisition cohorts and quantify retention, repeat purchase behavior, and customer value.

**Objective**  
Produce cohort tables and an executive interpretation.

**Dataset / Data Source**  
DR01 — UCI Online Retail; transaction dates and CustomerID are the core fields.

**Task**  
Design cohort month, retention matrix, repeat-rate curve, RFM summary, and segment-level revenue concentration. Explain cohort leakage risks.

**Technologies**  
Python + pandas + NumPy + Plotly + Excel

**Required Deliverables**  
Cohort table; RFM table; visualization set; assumptions document.

**Acceptance Criteria**  
Cohort assignment is deterministic; retention denominators are explicit; RFM features use only information available at cohort cutoff.

**Professional Skills Tested**  
Cohort analysis, RFM, time-aware feature construction

**Common Failure Modes**  
Using the first observed transaction as acquisition without stating the observation-window limitation; look-ahead in RFM.

**Production Considerations**  
Persist cohort logic in reusable SQL/Python transformations with tests.

**Extension Challenge**  
Estimate CLV under at least two transparent assumptions.

**Git Commit**  
`feat(analytics): add cohort retention and rfm`

**Portfolio Value**  
Demonstrates customer analytics beyond dashboards.

---

### Day 3 — SQL Revenue Mart with Window Functions

**Role**  
Data Analyst

**Business/Technical Scenario**  
Finance needs a reusable monthly revenue dataset rather than repeated ad-hoc queries.

**Problem Statement**  
Build a normalized-to-analytics SQL mart using CTEs and window functions.

**Objective**  
Answer ranking, month-over-month, and customer concentration questions in SQL.

**Dataset / Data Source**  
DR01; load into SQLite for local reproducibility; target tables: fact_sales, dim_customer, dim_product, dim_date.

**Task**  
Create a star-style analytical mart and solve 10 advanced questions: top products by month, rolling 30-day revenue, customer rank, share of revenue, first/last purchase.

**Technologies**  
SQLite + SQL + Python + SQLAlchemy

**Required Deliverables**  
schema.sql; transform.sql; validation queries; query README.

**Acceptance Criteria**  
All 10 queries return expected shapes; no accidental Cartesian joins; indexes documented; query plan reviewed for critical queries.

**Professional Skills Tested**  
Advanced SQL, dimensional modeling, query reasoning

**Common Failure Modes**  
Joining on text descriptions; window-frame mistakes; duplicate counting.

**Production Considerations**  
Move to PostgreSQL and add migrations and incremental loads.

**Extension Challenge**  
Add query-cost regression tests and materialized views.

**Git Commit**  
`feat(sql): build sales analytics mart`

**Portfolio Value**  
A reusable analytics-engineering artifact for GitHub.

---

### Day 4 — Statistical Quality Review of Sales Drivers

**Role**  
Data Scientist

**Business/Technical Scenario**  
A merchandising lead claims discounts increase order value.

**Problem Statement**  
Test the claim with defensible statistical analysis.

**Objective**  
Separate association from evidence of a meaningful effect.

**Dataset / Data Source**  
DR01; construct order-level discount proxies where justified; synthetic discount field may be added only if clearly labeled and not presented as original data.

**Task**  
Define hypotheses, choose tests, check assumptions, quantify effect sizes and confidence intervals, and document multiple-comparison considerations.

**Technologies**  
Python + SciPy + pandas + statsmodels

**Required Deliverables**  
statistical report; notebook; effect-size table; reproducibility script.

**Acceptance Criteria**  
Hypotheses pre-registered in markdown; assumptions checked; confidence intervals reported; practical significance discussed.

**Professional Skills Tested**  
Hypothesis testing, effect sizes, statistical reasoning

**Common Failure Modes**  
Fishing for significant p-values; ignoring dependence between repeated customer observations; equating significance with causality.

**Production Considerations**  
For production experimentation, use experiment design and exposure logging rather than retrospective observational claims.

**Extension Challenge**  
Repeat with a bootstrap-based robustness check.

**Git Commit**  
`feat(stats): evaluate discount-revenue hypothesis`

**Portfolio Value**  
Shows mature statistical interpretation instead of plot-only EDA.

---

### Day 5 — Management Dashboard with KPI Governance

**Role**  
BI Analyst

**Business/Technical Scenario**  
Executives consume different versions of revenue, AOV, and active-customer KPIs.

**Problem Statement**  
Create one governed dashboard with clear definitions and refresh-ready inputs.

**Objective**  
Make numbers consistent and decision-oriented.

**Dataset / Data Source**  
DR01; curated KPI dataset generated on Day 1–4.

**Task**  
Build a Power BI-equivalent dashboard in Power BI if available, otherwise Plotly/Streamlit; include revenue, orders, AOV, repeat rate, country mix, top products, anomaly flag.

**Technologies**  
Power BI or Streamlit + SQL + Python

**Required Deliverables**  
dashboard; KPI data dictionary; refresh script; screenshot pack.

**Acceptance Criteria**  
Every card maps to a documented query; filters do not change denominator definitions unexpectedly; refresh completes successfully.

**Professional Skills Tested**  
BI modeling, storytelling, semantic consistency

**Common Failure Modes**  
Overloading the page; hiding data quality caveats; inconsistent date grain.

**Production Considerations**  
Add row-level security and scheduled refresh in a real BI service.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(bi): publish governed sales dashboard`

**Portfolio Value**  
Portfolio-ready dashboard with data dictionary and architecture image.

---

### Day 6 — Automated Excel-to-Database Reconciliation

**Role**  
Data Analyst / Analytics Engineer

**Business/Technical Scenario**  
A finance team receives weekly Excel exports from multiple branches.

**Problem Statement**  
Automate reconciliation between spreadsheet totals and a canonical database.

**Objective**  
Detect mismatches before finance sign-off.

**Dataset / Data Source**  
Synthetic branch-sales workbook generated locally; labeled synthetic; 20–50k rows with intentional duplicate/missing-value cases.

**Task**  
Ingest Excel, validate schema/types, load to SQLite/PostgreSQL, reconcile totals and row counts, and produce an exceptions workbook.

**Technologies**  
Python + openpyxl + pandas + SQLite + SQLAlchemy

**Required Deliverables**  
ETL script; validation report; exception.xlsx; schema.sql; tests.

**Acceptance Criteria**  
Schema failures are explicit; reconciliation identifies injected defects; rerun is idempotent; logs contain run ID and counts.

**Professional Skills Tested**  
Data validation, ETL, Excel automation, idempotency

**Common Failure Modes**  
Trusting Excel types; silent coercion; non-idempotent inserts.

**Production Considerations**  
Add Great Expectations or equivalent data-quality checks and scheduled execution.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(data): automate excel reconciliation pipeline`

**Portfolio Value**  
Useful operations automation project with immediate business relevance.

---

### Day 7 — A/B Test Analysis for Checkout Conversion

**Role**  
Data Analyst

**Business/Technical Scenario**  
Product changed checkout UI and wants a decision on rollout.

**Problem Statement**  
Estimate the experiment effect without contaminating treatment/control groups.

**Objective**  
Recommend ship/hold based on conversion and guardrails.

**Dataset / Data Source**  
Synthetic A/B event dataset; explicitly synthetic; 200k+ sessions with experiment_id, variant, conversion, revenue.

**Task**  
Perform sample-ratio-mismatch checks, primary conversion analysis, confidence interval, practical effect threshold, and guardrail analysis for revenue/refunds.

**Technologies**  
Python + pandas + SciPy + statsmodels + Plotly

**Required Deliverables**  
experiment report; analysis notebook; decision table.

**Acceptance Criteria**  
Randomization health check documented; primary metric fixed before subgroup slicing; effect uncertainty shown; guardrails reviewed.

**Professional Skills Tested**  
Experimentation, causal inference basics, KPI design

**Common Failure Modes**  
peeking without correction; cherry-picked segments; ignoring SRM.

**Production Considerations**  
Production experimentation needs feature assignment logs, exposure events, stable bucketing, and audit trails.

**Extension Challenge**  
Implement sequential-testing-safe monitoring design.

**Git Commit**  
`feat(experiment): evaluate checkout ab test`

**Portfolio Value**  
Strong evidence of product analytics maturity.

---

### Day 8 — Forecasting Revenue with a Business Baseline

**Role**  
Data Scientist

**Business/Technical Scenario**  
Operations needs a six-week revenue forecast for staffing and purchasing.

**Problem Statement**  
Build and benchmark a time-series forecast against a naive baseline.

**Objective**  
Quantify whether the model actually improves business planning.

**Dataset / Data Source**  
DR04 — NYC TLC monthly trip records aggregated to daily demand proxy; official TLC source.

**Task**  
Create a daily series, backtest with rolling-origin evaluation, compare naive/seasonal-naive/ETS or equivalent, quantify MAE/WAPE, and explain forecast failure regions.

**Technologies**  
Python + pandas + statsmodels

**Required Deliverables**  
forecast pipeline; backtest notebook; forecast CSV; decision memo.

**Acceptance Criteria**  
Time-aware split; naive baseline included; metrics justified; prediction interval produced; no future leakage.

**Professional Skills Tested**  
Forecasting, backtesting, uncertainty

**Common Failure Modes**  
Random train/test split; tuning on the test period; ignoring calendar effects.

**Production Considerations**  
Deploy scheduled batch forecasts with versioned data snapshots and alerting on forecast degradation.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(forecast): establish demand forecasting baseline`

**Portfolio Value**  
Demonstrates business forecasting discipline.

---

### Day 9 — Customer Churn Modeling Blueprint

**Role**  
Data Scientist

**Business/Technical Scenario**  
A SaaS company needs early-warning signals for at-risk customers.

**Problem Statement**  
Define churn operationally and create a leakage-safe modeling dataset.

**Objective**  
Turn an ambiguous business request into a precise ML problem.

**Dataset / Data Source**  
Synthetic SaaS customer/event dataset; explicitly synthetic; 50k customers, event history and account snapshots.

**Task**  
Design churn label window, observation window, feature cutoff, candidate features, and data split strategy; do not train a final model yet.

**Technologies**  
Python + pandas + SQL + dbdiagram/ERD

**Required Deliverables**  
feature specification; SQL feature query; data dictionary; leakage checklist.

**Acceptance Criteria**  
Label definition is executable; every feature has an availability timestamp; temporal split is justified; target leakage tests included.

**Professional Skills Tested**  
Problem framing, feature stores concepts, leakage detection

**Common Failure Modes**  
Label leakage from cancellation timestamp; features computed after prediction time.

**Production Considerations**  
Promote features into an offline/online feature store when production scale requires it.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(ml): define leakage-safe churn dataset`

**Portfolio Value**  
Excellent demonstration of ML problem framing.

---

### Day 10 — Phase 1 Analytics Capstone — Executive BI Pack

**Role**  
BI Analyst / Data Scientist

**Business/Technical Scenario**  
Leadership needs one coherent view from raw transactions to action.

**Problem Statement**  
Consolidate Days 1–9 into a lightweight analytics product.

**Objective**  
Ship a reproducible business intelligence package.

**Dataset / Data Source**  
DR01 plus Day 6 synthetic reconciliation data where needed.

**Task**  
Integrate KPI definitions, cohort view, experiment readout, forecast baseline, and customer diagnostics into one decision pack.

**Technologies**  
Python + SQL + Streamlit/Power BI + Excel

**Required Deliverables**  
GitHub repo; dashboard; SQL; notebooks; tests; architecture diagram; executive memo; demo recording.

**Acceptance Criteria**  
Rebuild from a clean environment; data checks pass; KPI totals reconcile; README explains business assumptions and limitations.

**Professional Skills Tested**  
Analytics engineering, stakeholder communication, reproducibility

**Common Failure Modes**  
Copy-pasting notebook outputs; undocumented assumptions; no reproducibility path.

**Production Considerations**  
Use CI to lint/test data transformations and package the dashboard for deployment.

**Extension Challenge**  
Add automated daily refresh and Slack/email alerting.

**Git Commit**  
`feat(capstone): ship executive analytics platform`

**Portfolio Value**  
Capstone 1: Business Intelligence / Data Analytics Platform.

---

### Day 11 — Incremental API-to-Database Pipeline

**Role**  
Data Engineer

**Business/Technical Scenario**  
A logistics platform exposes shipment updates through an API.

**Problem Statement**  
Ingest incremental API data without duplicates or missed updates.

**Objective**  
Build a reliable ingestion job with checkpointing.

**Dataset / Data Source**  
Public REST API with stable test endpoint, or synthetic API service created locally; synthetic fallback must be labeled.

**Task**  
Implement paginated ingestion, cursor/watermark handling, retries with backoff, raw landing storage, and upsert into PostgreSQL.

**Technologies**  
Python + requests/httpx + PostgreSQL + SQLAlchemy

**Required Deliverables**  
pipeline package; raw JSON samples; SQL schema; logs; tests.

**Acceptance Criteria**  
Retries are bounded; reruns do not duplicate rows; checkpoint resumes after interruption; schema validation rejects malformed records.

**Professional Skills Tested**  
ETL/ELT, APIs, retries, idempotency

**Common Failure Modes**  
Using page number as durable state when records can shift; no timeout handling.

**Production Considerations**  
Add secrets management, rate-limit handling, orchestration, and dead-letter storage.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(ingest): add idempotent shipment api pipeline`

**Portfolio Value**  
Production-style data engineering artifact.

---

### Day 12 — Data Quality Contract and Validation Suite

**Role**  
Data Engineer

**Business/Technical Scenario**  
Finance data contains silently changing columns and bad categorical values.

**Problem Statement**  
Turn business expectations into executable data-quality contracts.

**Objective**  
Fail fast on critical defects while allowing quarantined noncritical records.

**Dataset / Data Source**  
Day 11 shipment data plus synthetic defect fixtures.

**Task**  
Implement schema, null, range, uniqueness, referential-integrity, and freshness checks; separate hard failures from quarantine cases.

**Technologies**  
Python + Pandera or Great Expectations + pytest

**Required Deliverables**  
quality module; expectation suite; quarantine sample; CI test output.

**Acceptance Criteria**  
Injected defects are detected deterministically; quality report identifies rule, field, count, severity; CI blocks critical failures.

**Professional Skills Tested**  
Data contracts, validation, testing, observability

**Common Failure Modes**  
Only checking nulls; validating after aggregates; not versioning rules.

**Production Considerations**  
Version data contracts alongside producers and use SLAs/SLOs for freshness and quality.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`test(data): enforce shipment data contracts`

**Portfolio Value**  
Strong data reliability signal.

---

### Day 13 — Star Schema for Supply-Chain Analytics

**Role**  
Data Engineer

**Business/Technical Scenario**  
A supply-chain team mixes shipment, vendor, product, and warehouse data.

**Problem Statement**  
Design an analytical warehouse model that supports stable business questions.

**Objective**  
Create fact/dimension tables with clear grain.

**Dataset / Data Source**  
Synthetic supply-chain dataset; explicitly synthetic; 1–5M fact rows target.

**Task**  
Define fact shipment grain, dimensions, surrogate keys, slowly changing dimension strategy, and 10 KPI queries.

**Technologies**  
PostgreSQL + SQL + dbdiagram

**Required Deliverables**  
ERD; DDL; seed data; KPI SQL; modeling decisions.

**Acceptance Criteria**  
Fact grain documented; no many-to-many ambiguity for core KPIs; dimensions support required filters.

**Professional Skills Tested**  
Dimensional modeling, SQL design, grain discipline

**Common Failure Modes**  
Mixing order and line-item grain; storing attributes that should be dimensions.

**Production Considerations**  
Use warehouse-specific partitioning and incremental materializations at scale.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(dw): model supply chain star schema`

**Portfolio Value**  
Portfolio-ready warehouse design artifact.

---

### Day 14 — Incremental ELT with Late-Arriving Events

**Role**  
Data Engineer

**Business/Technical Scenario**  
Orders arrive late or are corrected after daily loads.

**Problem Statement**  
Build an incremental transformation that handles late-arriving records.

**Objective**  
Preserve correctness under reprocessing.

**Dataset / Data Source**  
DR14 synthetic e-commerce events; 1–5M events with event_time and ingestion_time.

**Task**  
Create raw bronze, cleaned silver, and KPI gold layers; use ingestion watermark plus event-time correction window.

**Technologies**  
Python + DuckDB/Polars + PostgreSQL

**Required Deliverables**  
ELT scripts; test fixtures; KPI tables; runbook.

**Acceptance Criteria**  
Late events within the correction window update aggregates; outside-window behavior documented; reruns are deterministic.

**Professional Skills Tested**  
ELT, event-time semantics, batch processing

**Common Failure Modes**  
Using ingestion time as business time; duplicate corrections.

**Production Considerations**  
Add orchestration, state storage, backfill mode, and data lineage.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(elt): handle late arriving ecommerce events`

**Portfolio Value**  
Shows practical incremental-pipeline reasoning.

---

### Day 15 — Pipeline Observability and SLA Monitoring

**Role**  
Data Engineer / MLOps Engineer

**Business/Technical Scenario**  
A morning KPI dashboard is late and nobody knows why.

**Problem Statement**  
Add operational telemetry to the pipeline.

**Objective**  
Make pipeline health measurable.

**Dataset / Data Source**  
Days 11–14 pipelines; synthetic failure injections.

**Task**  
Emit run duration, record counts, freshness, failure reason, retry counts, and data-quality status; build a small health dashboard.

**Technologies**  
Python + structured logging + Prometheus concepts + Streamlit/Plotly

**Required Deliverables**  
metrics endpoint/file; monitoring dashboard; runbook; alert rules.

**Acceptance Criteria**  
Every run has correlation ID; metrics distinguish data failure vs infrastructure failure; at least three actionable alerts are defined.

**Professional Skills Tested**  
Observability, SLIs/SLOs, incident response

**Common Failure Modes**  
Logging huge raw payloads; no correlation IDs; alerts without action.

**Production Considerations**  
Route metrics to a real monitoring stack and define on-call severity levels.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(obs): instrument data pipeline health metrics`

**Portfolio Value**  
MLOps/data-platform portfolio differentiator.

---

### Day 16 — Batch Backfill and Recovery Drill

**Role**  
Data Engineer

**Business/Technical Scenario**  
A source outage caused three days of missing data.

**Problem Statement**  
Recover historical partitions without double-counting downstream KPIs.

**Objective**  
Prove a safe backfill workflow.

**Dataset / Data Source**  
DR14 synthetic event stream with intentionally removed partitions.

**Task**  
Implement partition-aware backfill, checkpointing, reconciliation before/after, and a recovery runbook.

**Technologies**  
Python + DuckDB/PostgreSQL + Bash

**Required Deliverables**  
backfill script; recovery report; runbook; tests.

**Acceptance Criteria**  
Backfill restores expected counts; downstream aggregates are correct; rerun is safe.

**Professional Skills Tested**  
Recovery engineering, idempotency, operational thinking

**Common Failure Modes**  
Manual CSV replacement; deleting and reloading all history unnecessarily.

**Production Considerations**  
Automate replay with Airflow/Prefect/Dagster or cloud-native scheduler.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`fix(data): implement partition backfill and recovery`

**Portfolio Value**  
Demonstrates incident-ready engineering.

---

### Day 17 — PostgreSQL Query Optimization Investigation

**Role**  
Database Engineer

**Business/Technical Scenario**  
A customer dashboard query that once ran in seconds now takes minutes.

**Problem Statement**  
Diagnose the root cause and improve query performance.

**Objective**  
Use evidence from execution plans, not guesswork.

**Dataset / Data Source**  
Synthetic PostgreSQL schema from Day 13; 1–5M rows.

**Task**  
Profile slow query with EXPLAIN ANALYZE, test indexes, rewrite joins/CTEs where justified, and document before/after performance.

**Technologies**  
PostgreSQL + SQL + Python benchmark script

**Required Deliverables**  
before.sql; after.sql; EXPLAIN plans; benchmark report.

**Acceptance Criteria**  
At least one bottleneck is identified from evidence; median/p95 latency improves materially on the benchmark; correctness preserved.

**Professional Skills Tested**  
Query optimization, indexing, benchmarking

**Common Failure Modes**  
Adding random indexes; optimizing without measurements; changing semantics.

**Production Considerations**  
Use workload-aware indexing, statistics maintenance, partitioning, or read replicas where appropriate.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`perf(sql): optimize supply chain dashboard query`

**Portfolio Value**  
Excellent database-engineering evidence.

---

### Day 18 — Data Versioning with DVC

**Role**  
Data Engineer / ML Engineer

**Business/Technical Scenario**  
An ML team cannot reproduce the dataset used for last month's model.

**Problem Statement**  
Version large data artifacts and tie them to code commits.

**Objective**  
Make dataset lineage reproducible.

**Dataset / Data Source**  
Small/medium synthetic tabular dataset plus Day 9 churn features; synthetic where applicable.

**Task**  
Initialize DVC, create reproducible data stages, document remote-storage strategy, and prove checkout of an older dataset version.

**Technologies**  
Git + DVC + Python

**Required Deliverables**  
DVC config; pipeline stages; data manifest; reproducibility demo notes.

**Acceptance Criteria**  
A clean checkout can reconstruct the dataset used by a tagged commit; no secrets committed.

**Professional Skills Tested**  
Data versioning, lineage, reproducibility

**Common Failure Modes**  
Tracking data binaries directly in Git; mutable file paths; no manifest.

**Production Considerations**  
Use object storage with access controls and retention policies.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`chore(mlops): version training data with dvc`

**Portfolio Value**  
Professional MLOps foundation artifact.

---

### Day 19 — Automated KPI Report Generator

**Role**  
Analytics Engineer

**Business/Technical Scenario**  
Management wants the weekly performance pack automatically emailed.

**Problem Statement**  
Create deterministic report generation from curated data.

**Objective**  
Turn analytics into a repeatable service.

**Dataset / Data Source**  
Day 5 KPI dataset plus synthetic current-period updates.

**Task**  
Generate HTML/PDF-like report pages or a static dashboard snapshot with trend commentary generated from deterministic rules.

**Technologies**  
Python + pandas + Jinja2 + Plotly + scheduled task

**Required Deliverables**  
report generator; sample report; scheduler config; test fixtures.

**Acceptance Criteria**  
Same input produces same report; missing data is flagged; report generation completes noninteractively.

**Professional Skills Tested**  
Automation, reporting, templating

**Common Failure Modes**  
Hard-coded date ranges; silent failures; manually edited charts.

**Production Considerations**  
Add artifact storage, signed reports, and distribution controls.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(reporting): automate weekly performance pack`

**Portfolio Value**  
Strong business-automation portfolio item.

---

### Day 20 — Phase 2 Capstone — Reliable Analytics Data Platform

**Role**  
Data Engineer

**Business/Technical Scenario**  
The organization wants a trusted, refreshable analytics foundation.

**Problem Statement**  
Combine ingestion, quality, modeling, monitoring, and reporting into one system.

**Objective**  
Ship an end-to-end analytics platform with operational controls.

**Dataset / Data Source**  
DR14 synthetic e-commerce stream + public source metadata where appropriate.

**Task**  
Build raw→clean→mart pipeline, quality gates, incremental processing, observability, report generation, and recovery procedure.

**Technologies**  
Python + PostgreSQL + DuckDB + DVC + GitHub Actions

**Required Deliverables**  
repo; pipeline; schemas; tests; monitoring dashboard; runbook; architecture diagram; demo.

**Acceptance Criteria**  
Cold-start setup documented; pipeline is idempotent; critical quality checks pass; backfill works; CI green.

**Professional Skills Tested**  
Data engineering, reliability, DevOps

**Common Failure Modes**  
One giant script; no retry strategy; no data contract.

**Production Considerations**  
Deploy scheduled jobs on free/local infrastructure first; later map components to AWS/Azure/GCP managed equivalents.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(capstone): ship reliable analytics data platform`

**Portfolio Value**  
Capstone 1 extension / enterprise-grade analytics engineering centerpiece.

---

### Day 21 — Regression for Revenue Planning

**Role**  
Data Scientist

**Business/Technical Scenario**  
A retailer needs expected basket revenue before fulfillment.

**Problem Statement**  
Build a leakage-safe regression model and quantify business impact.

**Objective**  
Predict order value with interpretable baselines first.

**Dataset / Data Source**  
DR03-style physicochemical data is not business-aligned; use a synthetic order-level dataset explicitly generated for this day, 50k rows.

**Task**  
Compare linear regression, regularized regression, tree-based model; use cross-validation and error segmentation by order size.

**Technologies**  
Python + pandas + scikit-learn + XGBoost

**Required Deliverables**  
training script; validation report; model card; error analysis.

**Acceptance Criteria**  
Temporal or grouped split where required; MAE/RMSE and business loss shown; leakage checks documented.

**Professional Skills Tested**  
Regression, baselines, evaluation, error analysis

**Common Failure Modes**  
Scaling leakage; random split across same customer; evaluating only average metric.

**Production Considerations**  
Package preprocessing and model as a single reproducible pipeline.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(ml): build revenue regression baseline`

**Portfolio Value**  
Demonstrates model selection for a business objective.

---

### Day 22 — Classification with Threshold Economics

**Role**  
Data Scientist

**Business/Technical Scenario**  
A bank wants to prioritize customers for a retention campaign.

**Problem Statement**  
Predict a binary outcome and optimize decision threshold by business cost.

**Objective**  
Move beyond default 0.5 classification.

**Dataset / Data Source**  
DR02 — UCI Bank Marketing; 45,211 rows; target y; 16 input features in classic version.

**Task**  
Train logistic regression and tree ensemble; evaluate ROC-AUC/PR-AUC; calibrate probabilities; choose threshold from explicit campaign economics.

**Technologies**  
Python + pandas + scikit-learn + calibration tools

**Required Deliverables**  
model package; threshold report; confusion-cost table.

**Acceptance Criteria**  
No target leakage from duration if deployment timing would exclude it; calibration assessed; threshold justified from costs.

**Professional Skills Tested**  
Classification, calibration, decision theory

**Common Failure Modes**  
Using accuracy on imbalanced data; using post-outcome features.

**Production Considerations**  
Store threshold as versioned config and monitor drift of score and outcome rates.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(ml): optimize bank campaign decision threshold`

**Portfolio Value**  
Strong real dataset classification artifact.

---

### Day 23 — Leakage Audit on an Educational Predictor

**Role**  
Data Scientist

**Business/Technical Scenario**  
A university wants to predict student dropout at enrollment time.

**Problem Statement**  
Build a classifier using only features available at the decision point.

**Objective**  
Detect and remove temporal leakage.

**Dataset / Data Source**  
DR07 — UCI Predict Students' Dropout and Academic Success; 4,424 rows; multiclass target.

**Task**  
Create an availability matrix, audit suspicious fields, compare leaked vs leakage-safe models, and document the difference.

**Technologies**  
Python + pandas + scikit-learn

**Required Deliverables**  
leakage audit; two pipelines; comparison report.

**Acceptance Criteria**  
Every retained feature has a documented timestamp/availability rationale; leaked benchmark clearly labeled as invalid.

**Professional Skills Tested**  
Leakage detection, temporal reasoning, model governance

**Common Failure Modes**  
Keeping semester-outcome features because they boost F1.

**Production Considerations**  
Make feature contracts enforce allowed-time fields in training pipelines.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(ml): harden dropout model against leakage`

**Portfolio Value**  
Excellent senior-level modeling judgment.

---

### Day 24 — Model Comparison: XGBoost vs LightGBM vs CatBoost

**Role**  
ML Engineer

**Business/Technical Scenario**  
A tabular classification service must balance performance, training time, and categorical handling.

**Problem Statement**  
Benchmark three gradient-boosting families under a common evaluation protocol.

**Objective**  
Produce a fair benchmark rather than a leaderboard chase.

**Dataset / Data Source**  
DR02 bank marketing; stratified temporal-aware evaluation plan.

**Task**  
Standardize preprocessing where appropriate, tune modestly, record training/inference cost, and compare calibration and PR-AUC.

**Technologies**  
Python + scikit-learn + XGBoost + LightGBM + CatBoost

**Required Deliverables**  
benchmark table; experiment configs; plots; model selection memo.

**Acceptance Criteria**  
Same split and primary metric across models; random seeds logged; timing measured; best model selected with multi-factor rationale.

**Professional Skills Tested**  
Benchmarking, experiment hygiene, model selection

**Common Failure Modes**  
Changing validation set per model; over-tuning one model; ignoring latency.

**Production Considerations**  
Create a reproducible benchmark runner with MLflow later.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(bench): compare gradient boosting libraries`

**Portfolio Value**  
High-signal ML engineering artifact.

---

### Day 25 — Imbalanced Classification with Cost-Sensitive Learning

**Role**  
ML Engineer

**Business/Technical Scenario**  
Fraud operations has few positives and expensive false negatives.

**Problem Statement**  
Improve minority-class detection while controlling false-positive workload.

**Objective**  
Optimize for operational constraints.

**Dataset / Data Source**  
Synthetic fraud transaction dataset, explicitly synthetic, 200k rows, <2% fraud.

**Task**  
Compare class weights, undersampling, threshold optimization, and balanced ensemble; report PR-AUC, recall at precision target, and alert volume.

**Technologies**  
Python + scikit-learn + imbalanced-learn

**Required Deliverables**  
benchmark; threshold policy; confusion-cost analysis; test set.

**Acceptance Criteria**  
Test set untouched until final comparison; alert-volume constraint respected; minority performance stable across folds.

**Professional Skills Tested**  
Imbalance, thresholding, operational metrics

**Common Failure Modes**  
SMOTE before split; accuracy obsession; optimizing only recall.

**Production Considerations**  
Add delayed-label monitoring and investigator feedback loop.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(fraud): build cost-sensitive classification pipeline`

**Portfolio Value**  
Realistic fintech ML case.

---

### Day 26 — Research Day — Reproduce a Tabular ML Paper

**Role**  
Research Engineer

**Business/Technical Scenario**  
You need to learn whether a published tabular-ML claim holds under a clean reproduction.

**Problem Statement**  
Reproduce one reported result from a peer-reviewed/public paper using an available public dataset.

**Objective**  
Practice scientific reproducibility, not citation theater.

**Dataset / Data Source**  
Use DR02 or DR03 plus a real paper selected from the dataset documentation/related-work chain; verify paper source before coding.

**Task**  
Research question → background → related work → dataset → baseline → reproduction experiment → metrics → results → error analysis → limitations → future work.

**Technologies**  
Python + scikit-learn + paper implementation + MLflow-lite logging

**Required Deliverables**  
reproduction report; exact citation; code; environment lock; result table; deviation log.

**Acceptance Criteria**  
Paper, dataset, and experimental protocol are cited and verified; no fabricated numbers; deviations from paper are explicit.

**Professional Skills Tested**  
Literature review, reproducibility, experiment design

**Common Failure Modes**  
Copying reported metrics as if reproduced; untracked preprocessing differences.

**Production Considerations**  
Pin dependencies and use dataset hashes/configs.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`research: reproduce tabular ml baseline`

**Portfolio Value**  
Research portfolio artifact with transparent methodology.

---

### Day 27 — Feature Engineering Under a Compute Budget

**Role**  
ML Engineer

**Business/Technical Scenario**  
A model is accurate but feature generation is too expensive for daily scoring.

**Problem Statement**  
Redesign features to preserve signal under latency and memory constraints.

**Objective**  
Optimize the whole feature pipeline, not only the model.

**Dataset / Data Source**  
Synthetic churn event dataset from Day 9; 1M+ events target.

**Task**  
Profile feature generation, replace expensive joins with aggregates/materialized tables, benchmark CPU/memory, and compare model quality.

**Technologies**  
Python + pandas/Polars + PostgreSQL + scikit-learn

**Required Deliverables**  
profiling report; optimized feature job; benchmark; model comparison.

**Acceptance Criteria**  
Feature build time and memory materially improve without unacceptable model degradation; same labels and split used.

**Professional Skills Tested**  
Feature engineering, profiling, systems thinking

**Common Failure Modes**  
Premature optimization; caching stale features without timestamps.

**Production Considerations**  
Introduce feature-store concepts with point-in-time correctness.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`perf(features): optimize churn feature generation`

**Portfolio Value**  
Shows production constraints awareness.

---

### Day 28 — Unsupervised Customer Segmentation

**Role**  
Data Scientist

**Business/Technical Scenario**  
Marketing wants segments but has no trustworthy labels.

**Problem Statement**  
Create actionable segments from customer behavior.

**Objective**  
Build stable clusters and interpret them for business use.

**Dataset / Data Source**  
DR01 Online Retail; customer-level RFM features.

**Task**  
Compare K-Means, hierarchical clustering, and DBSCAN; assess stability and business interpretability; name segments using behavior, not arbitrary personas.

**Technologies**  
Python + pandas + scikit-learn + scipy + Plotly

**Required Deliverables**  
cluster notebook; stability analysis; segment table; business recommendations.

**Acceptance Criteria**  
Scale features properly; cluster count justified; stability tested; outliers investigated.

**Professional Skills Tested**  
Clustering, dimensionality reduction, interpretation

**Common Failure Modes**  
Choosing k only from elbow plot; scaling forgotten; treating clusters as truth.

**Production Considerations**  
Monitor segment drift and establish re-segmentation cadence.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(ml): create behavior-based customer segments`

**Portfolio Value**  
Good unsupervised analytics story.

---

### Day 29 — DBSCAN for Operational Anomaly Discovery

**Role**  
Data Scientist

**Business/Technical Scenario**  
Logistics has unusual delivery records that are not captured by business labels.

**Problem Statement**  
Use density-based methods to flag unusual behavior without a fixed cluster count.

**Objective**  
Assess anomaly utility rather than novelty alone.

**Dataset / Data Source**  
Synthetic delivery telemetry, explicitly synthetic; 100k records.

**Task**  
Engineer time/distance/cost features; compare DBSCAN/Isolation Forest; review top anomalies against business rules.

**Technologies**  
Python + scikit-learn + Plotly

**Required Deliverables**  
anomaly dataset; top-anomaly report; comparison chart.

**Acceptance Criteria**  
Parameters documented; anomaly review includes false-positive analysis; no claim of truth from unsupervised labels alone.

**Professional Skills Tested**  
Anomaly detection, operational review

**Common Failure Modes**  
Using Euclidean distance on unscaled features; equating rare with fraudulent.

**Production Considerations**  
Create human feedback loop and monitor anomaly-rate drift.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(anomaly): add density based delivery anomaly detection`

**Portfolio Value**  
Shows practical unsupervised ML.

---

### Day 30 — PCA and Feature Compression for Serving

**Role**  
ML Engineer

**Business/Technical Scenario**  
Inference payloads have dozens of correlated numeric signals and bandwidth is constrained.

**Problem Statement**  
Test dimensionality reduction while preserving model utility.

**Objective**  
Measure the trade-off between compression and accuracy.

**Dataset / Data Source**  
DR03 Wine Quality or synthetic high-dimensional version derived without fabricating labels.

**Task**  
Compare raw features vs PCA-whitened representations across linear and tree models; evaluate explained variance and downstream metrics.

**Technologies**  
Python + scikit-learn

**Required Deliverables**  
experiment report; PCA pipeline; latency/size benchmark.

**Acceptance Criteria**  
PCA fit only on training folds; component count justified; downstream metric delta quantified.

**Professional Skills Tested**  
Representation learning, leakage prevention, compression

**Common Failure Modes**  
Fitting PCA on all data; assuming explained variance equals predictive usefulness.

**Production Considerations**  
Version PCA transform with the model and validate schema at inference.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(ml): benchmark pca feature compression`

**Portfolio Value**  
Useful for understanding serving constraints.

---

### Day 31 — Hyperparameter Optimization with Optuna

**Role**  
ML Engineer

**Business/Technical Scenario**  
The baseline model plateaus and manual tuning is inconsistent.

**Problem Statement**  
Set up a reproducible hyperparameter search with an explicit optimization target.

**Objective**  
Optimize performance without overfitting the validation design.

**Dataset / Data Source**  
DR02 or synthetic fraud dataset from Day 25.

**Task**  
Build Optuna study, pruning, search-space rationale, fixed validation protocol, and final untouched test evaluation.

**Technologies**  
Python + Optuna + scikit-learn/XGBoost

**Required Deliverables**  
study database; best config; optimization history; final evaluation.

**Acceptance Criteria**  
Search budget fixed; objective defined once; test set touched once; study reproducible enough to audit.

**Professional Skills Tested**  
HPO, experiment tracking, evaluation rigor

**Common Failure Modes**  
Optimizing on test data; giant search budget; unstable random seeds.

**Production Considerations**  
Persist studies and model artifacts; integrate with MLflow.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(hpo): add optuna model optimization`

**Portfolio Value**  
Core production ML workflow.

---

### Day 32 — SHAP-Based Model Explanation for Operations

**Role**  
ML Engineer

**Business/Technical Scenario**  
Risk analysts need reasons for model scores.

**Problem Statement**  
Provide global and local explanations that align with model behavior.

**Objective**  
Build an explanation layer with caveats.

**Dataset / Data Source**  
DR02 bank marketing or Day 25 fraud model.

**Task**  
Generate SHAP global importance, dependence views, and case-level explanations; compare to permutation importance and investigate counterintuitive cases.

**Technologies**  
Python + SHAP + scikit-learn/XGBoost

**Required Deliverables**  
explainability report; example cases; limitations note.

**Acceptance Criteria**  
Explanations reproduce model outputs; no causal claims; sensitive-feature handling documented.

**Professional Skills Tested**  
Interpretability, model governance

**Common Failure Modes**  
Calling feature importance causal; displaying unstable local explanations as facts.

**Production Considerations**  
Log explanation versions and access-control sensitive customer-level details.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(explain): add shap model explanations`

**Portfolio Value**  
Portfolio artifact showing responsible model interpretation.

---

### Day 33 — Research Day — Ablation Study on Feature Groups

**Role**  
Research Engineer

**Business/Technical Scenario**  
A model uses many engineered signals, but stakeholders want to know which groups actually matter.

**Problem Statement**  
Run a controlled ablation study over feature families.

**Objective**  
Quantify contribution and interaction under a fixed evaluation protocol.

**Dataset / Data Source**  
Day 27 churn or Day 25 fraud dataset; groups: demographics, behavioral aggregates, monetary, recency.

**Task**  
Research protocol: baseline → remove one group at a time → repeat over fixed folds → compare metrics and confidence intervals → analyze errors.

**Technologies**  
Python + scikit-learn + MLflow + statsmodels

**Required Deliverables**  
ablation matrix; plots; research report; configs.

**Acceptance Criteria**  
Only one factor changes per experiment; folds/seed fixed; uncertainty reported; conclusions tied to measured deltas.

**Professional Skills Tested**  
Ablation design, scientific reasoning, reproducibility

**Common Failure Modes**  
Changing model as feature groups change; over-interpreting small deltas.

**Production Considerations**  
Automate experiment matrices and archive configs/artifacts.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`research: quantify feature group ablations`

**Portfolio Value**  
Strong research-engineering evidence.

---

### Day 34 — Model Error Analysis Lab

**Role**  
Data Scientist

**Business/Technical Scenario**  
A production model misses specific customer segments despite good aggregate metrics.

**Problem Statement**  
Build an error taxonomy and prioritize fixes.

**Objective**  
Turn false positives/negatives into engineering hypotheses.

**Dataset / Data Source**  
Day 22 or 25 held-out predictions.

**Task**  
Slice errors by customer tenure, region, score band, missingness, class, and data-quality flags; identify top failure modes and propose targeted changes.

**Technologies**  
Python + pandas + Plotly + scikit-learn

**Required Deliverables**  
error-analysis notebook; slice report; prioritized remediation plan.

**Acceptance Criteria**  
Every slice has support count; no p-hacking via hundreds of unreported slices; top errors manually inspected.

**Professional Skills Tested**  
Error analysis, robustness, fairness-aware diagnostics

**Common Failure Modes**  
Tiny slices presented as conclusions; ignoring selection bias.

**Production Considerations**  
Instrument production predictions so the same taxonomy can run continuously.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(ml): add structured model error analysis`

**Portfolio Value**  
Very interview-relevant professional practice.

---

### Day 35 — Phase 3 Capstone — Customer Risk Decision Engine

**Role**  
ML Engineer

**Business/Technical Scenario**  
A SaaS business needs a model-driven customer retention queue.

**Problem Statement**  
Ship a complete supervised ML solution from data to decision.

**Objective**  
Demonstrate framing, training, thresholding, explanation, and packaging.

**Dataset / Data Source**  
Synthetic churn events + Day 9 feature design; explicitly synthetic.

**Task**  
Implement point-in-time features, baseline + tuned model, calibration, threshold policy, SHAP review, error analysis, and batch scoring command.

**Technologies**  
Python + scikit-learn + Optuna + SHAP + SQL

**Required Deliverables**  
package; batch scorer; model card; tests; report; sample scores.

**Acceptance Criteria**  
Reproducible training; leakage tests; threshold documented; minimum unit/integration tests; artifact version stored.

**Professional Skills Tested**  
End-to-end ML, software engineering, governance

**Common Failure Modes**  
Training inside notebook only; hidden preprocessing; no deterministic run command.

**Production Considerations**  
Prepare service boundary for FastAPI and MLflow in Phase 4.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(capstone): ship customer risk decision engine`

**Portfolio Value**  
Capstone 2: End-to-End Machine Learning System.

---

### Day 36 — Refactor Notebook into Production Package

**Role**  
ML Engineer

**Business/Technical Scenario**  
A promising notebook has been approved for a pilot.

**Problem Statement**  
Convert exploratory code into a maintainable Python package.

**Objective**  
Separate data, features, model, configuration, and CLI concerns.

**Dataset / Data Source**  
Day 35 capstone codebase.

**Task**  
Refactor into src/ layout with type hints, configuration, logging, tests, and a train/evaluate/predict CLI.

**Technologies**  
Python + pyproject.toml + pytest + pydantic

**Required Deliverables**  
package; CLI; unit tests; README; migration notes.

**Acceptance Criteria**  
Clean install works; CLI can train/evaluate/predict; core functions typed and tested; no notebook-only dependencies.

**Professional Skills Tested**  
Software engineering, packaging, testing

**Common Failure Modes**  
Global state; hidden file paths; duplicated transformation logic.

**Production Considerations**  
Add semantic versioning and build/publish workflow.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`refactor(ml): convert notebook pipeline to package`

**Portfolio Value**  
Major professional engineering milestone.

---

### Day 37 — FastAPI Model Serving Service

**Role**  
ML Engineer

**Business/Technical Scenario**  
The retention engine must provide real-time risk scores to a web application.

**Problem Statement**  
Expose validated model inference through a REST API.

**Objective**  
Build a small but production-shaped service.

**Dataset / Data Source**  
Day 36 package and model artifact.

**Task**  
Create /health, /predict, /metadata endpoints; validate input schema; version model; return probability and decision.

**Technologies**  
FastAPI + Pydantic + Uvicorn + Python

**Required Deliverables**  
API source; OpenAPI docs; tests; example curl; model artifact strategy.

**Acceptance Criteria**  
Invalid payloads return 4xx; health endpoint independent of model; response schema stable; integration tests pass.

**Professional Skills Tested**  
API engineering, validation, service design

**Common Failure Modes**  
Loading model per request; unbounded payloads; no version metadata.

**Production Considerations**  
Add auth, rate limiting, structured logs, metrics, and graceful shutdown.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(api): serve risk model with fastapi`

**Portfolio Value**  
Portfolio-ready ML API.

---

### Day 38 — MLflow Experiment Tracking and Registry

**Role**  
MLOps Engineer

**Business/Technical Scenario**  
Multiple candidate models exist with unclear lineage.

**Problem Statement**  
Track experiments, register a champion, and record artifacts.

**Objective**  
Make model selection auditable.

**Dataset / Data Source**  
Day 35/36 model runs.

**Task**  
Log parameters, metrics, dataset version, code commit, model artifacts, and tags; register candidate and promotion process.

**Technologies**  
MLflow + Python + Git + DVC

**Required Deliverables**  
MLflow screenshots/export; registry policy; promotion script; README.

**Acceptance Criteria**  
Runs can be traced to code/data; model version carries metadata; promotion is explicit.

**Professional Skills Tested**  
Experiment tracking, registry, lineage

**Common Failure Modes**  
Logging metrics manually; no dataset/version linkage.

**Production Considerations**  
Use a managed tracking server only when needed; protect registry access.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(mlops): add mlflow tracking and registry`

**Portfolio Value**  
Core MLOps portfolio piece.

---

### Day 39 — Production Debugging — Accuracy Collapse

**Role**  
MLOps Engineer

**Business/Technical Scenario**  
A deployed churn model's F1 drops sharply after a new customer onboarding campaign.

**Problem Statement**  
Diagnose whether the issue is data drift, label delay, pipeline breakage, or model behavior.

**Objective**  
Find root cause using evidence, not guesswork.

**Dataset / Data Source**  
Synthetic incident package containing historical predictions, current features, schema versions, and a hidden injected fault.

**Task**  
Inspect feature distributions, null rates, label arrival timing, score distributions, and pipeline versions; identify the root cause and corrective action.

**Technologies**  
Python + pandas + MLflow + Plotly + logs

**Required Deliverables**  
incident report; root-cause evidence; patch; regression test.

**Acceptance Criteria**  
Root cause supported by at least three independent signals; fix prevents recurrence; no model retraining until cause understood.

**Professional Skills Tested**  
Production diagnosis, observability, incident response

**Common Failure Modes**  
Immediately retraining; changing threshold without diagnosis.

**Production Considerations**  
Define runbook, alert thresholds, and model health SLOs.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`fix(mlops): resolve production accuracy incident`

**Portfolio Value**  
Shows operational ML maturity.

---

### Day 40 — Dockerize the ML Service

**Role**  
DevOps / ML Engineer

**Business/Technical Scenario**  
The API works locally but needs repeatable deployment.

**Problem Statement**  
Containerize service and model dependencies.

**Objective**  
Achieve reproducible runtime behavior.

**Dataset / Data Source**  
Day 37 FastAPI service.

**Task**  
Create non-root Docker image, health check, .dockerignore, deterministic dependency install, and local run command.

**Technologies**  
Docker + FastAPI + Python

**Required Deliverables**  
Dockerfile; compose config; image build notes; health test.

**Acceptance Criteria**  
Container builds from clean context; health check passes; service accessible; secrets not baked into image.

**Professional Skills Tested**  
Containers, dependency management, security basics

**Common Failure Modes**  
Running as root; copying .env; huge base image.

**Production Considerations**  
Use multi-stage builds, SBOM/scanning, resource limits, and image promotion.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`chore(devops): containerize ml inference api`

**Portfolio Value**  
Foundational deployment artifact.

---

### Day 41 — CI Pipeline for Tests, Linting, and Build

**Role**  
DevOps Engineer

**Business/Technical Scenario**  
Pull requests routinely break the inference API.

**Problem Statement**  
Create GitHub Actions CI gates.

**Objective**  
Prevent regressions before merge.

**Dataset / Data Source**  
Day 40 repo.

**Task**  
Run formatting/lint/type checks, unit/integration tests, Docker build, and artifact checks on PRs.

**Technologies**  
GitHub Actions + pytest + ruff + mypy + Docker

**Required Deliverables**  
workflow YAML; badge; branch protection recommendation; test report.

**Acceptance Criteria**  
CI fails on broken tests/type/lint/build; runs on PR and main; no credentials exposed.

**Professional Skills Tested**  
CI/CD, quality gates, Git practices

**Common Failure Modes**  
Only testing on main; flaky tests; secrets in logs.

**Production Considerations**  
Add caching, dependency audit, coverage trend, and release workflow.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`ci: add ml service quality gates`

**Portfolio Value**  
Professional GitHub practice.

---

### Day 42 — Environment Configuration and Secret Hygiene

**Role**  
DevOps Engineer

**Business/Technical Scenario**  
The app needs different settings across local, CI, and production.

**Problem Statement**  
Separate configuration from code and eliminate secret leakage paths.

**Objective**  
Make deployment configuration explicit and safe.

**Dataset / Data Source**  
Day 40 service.

**Task**  
Implement typed environment configuration, .env.example, CI secrets mapping, and pre-commit secret scanning.

**Technologies**  
Python + Pydantic Settings + GitHub Actions

**Required Deliverables**  
config module; .env.example; scanner config; docs.

**Acceptance Criteria**  
No credentials in Git history; missing required envs fail clearly; config differs by environment without code changes.

**Professional Skills Tested**  
Configuration management, secrets handling

**Common Failure Modes**  
Defaulting production secrets to placeholders; logging secret values.

**Production Considerations**  
Use cloud secret managers or platform secrets for deployed environments.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`chore(security): harden application configuration`

**Portfolio Value**  
Security-aware engineering artifact.

---

### Day 43 — Real-Time Inference Load Test

**Role**  
Performance Engineer / ML Engineer

**Business/Technical Scenario**  
The scoring endpoint becomes slow during campaign spikes.

**Problem Statement**  
Measure throughput, latency, and resource usage under concurrency.

**Objective**  
Set evidence-based performance targets.

**Dataset / Data Source**  
Day 40 containerized service + representative synthetic payloads.

**Task**  
Run controlled load test; measure p50/p95/p99 latency, throughput, CPU/memory, error rate; identify bottleneck.

**Technologies**  
Python + Locust/k6 + Docker

**Required Deliverables**  
load-test script; benchmark report; bottleneck analysis.

**Acceptance Criteria**  
Test is repeatable; p95 and error rate reported; workload assumptions explicit; regression threshold added to docs.

**Professional Skills Tested**  
Performance engineering, benchmarking

**Common Failure Modes**  
Testing only one request; warm-up ignored; measuring client time incorrectly.

**Production Considerations**  
Add autoscaling policy and model caching/batching where architecture supports it.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`perf(api): benchmark real time inference latency`

**Portfolio Value**  
Excellent production-readiness signal.

---

### Day 44 — Research Day — Model Calibration Benchmark

**Role**  
Research Engineer

**Business/Technical Scenario**  
Risk scores are used as probabilities but calibration is unknown.

**Problem Statement**  
Benchmark calibration methods under a fixed evaluation protocol.

**Objective**  
Determine whether probability estimates can support expected-cost decisions.

**Dataset / Data Source**  
DR02 or Day 25 fraud dataset with train/validation/test splits.

**Task**  
Compare uncalibrated model, Platt/sigmoid, isotonic; evaluate Brier score, reliability curves, and decision-cost sensitivity.

**Technologies**  
Python + scikit-learn + matplotlib/Plotly

**Required Deliverables**  
research report; calibration plots; method comparison; reproducibility config.

**Acceptance Criteria**  
Calibration fitted only on train/validation; test used once; class imbalance accounted for.

**Professional Skills Tested**  
Probabilistic modeling, calibration, experimental design

**Common Failure Modes**  
Calibrating on test data; judging by ROC-AUC only.

**Production Considerations**  
Monitor calibration drift in production and recalibrate safely.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`research: benchmark probability calibration methods`

**Portfolio Value**  
Research-quality applied ML artifact.

---

### Day 45 — Model Versioned Batch Inference Job

**Role**  
MLOps Engineer

**Business/Technical Scenario**  
Operations needs a nightly file of risk scores.

**Problem Statement**  
Build a batch scoring job with versioned inputs/outputs.

**Objective**  
Make batch inference restartable and auditable.

**Dataset / Data Source**  
Day 35 model + synthetic nightly customer snapshot.

**Task**  
Load registered model version, validate input schema, score in chunks, write output with model/data version metadata, and reconcile counts.

**Technologies**  
Python + MLflow + pandas/Polars + PostgreSQL

**Required Deliverables**  
CLI job; sample output; reconciliation report; runbook.

**Acceptance Criteria**  
Exactly-once output partition strategy; scores tied to model version; invalid rows quarantined.

**Professional Skills Tested**  
Batch inference, lineage, auditability

**Common Failure Modes**  
Overwriting outputs without versioning; loading all data in memory.

**Production Considerations**  
Schedule via cron/Airflow/Prefect and publish metrics to monitoring.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(batch): add versioned nightly inference job`

**Portfolio Value**  
Complete lifecycle component.

---

### Day 46 — Production Debugging — SQL Regression

**Role**  
Data Engineer

**Business/Technical Scenario**  
A feature query goes from 2s to 45s after a new index migration.

**Problem Statement**  
Identify the cause and roll out a safe correction.

**Objective**  
Practice database incident response.

**Dataset / Data Source**  
Day 17 schema + a synthetic migration introducing regression.

**Task**  
Compare plans before/after, inspect index statistics and join cardinality, revert/alter index, and add a performance regression test.

**Technologies**  
PostgreSQL + EXPLAIN + Python benchmark

**Required Deliverables**  
incident report; migration fix; regression benchmark; rollback notes.

**Acceptance Criteria**  
Measured improvement; no correctness regression; rollback path documented.

**Professional Skills Tested**  
Database operations, change management

**Common Failure Modes**  
Adding more indexes blindly; skipping rollback plan.

**Production Considerations**  
Use migrations in CI with representative explain-plan checks.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`fix(db): resolve feature query performance regression`

**Portfolio Value**  
Very realistic production-debugging artifact.

---

### Day 47 — Data Drift and Concept Drift Monitor

**Role**  
MLOps Engineer

**Business/Technical Scenario**  
Customer behavior changes after a pricing update.

**Problem Statement**  
Detect distribution shifts and separate them from outcome-performance degradation.

**Objective**  
Create a monitoring design with actionable thresholds.

**Dataset / Data Source**  
Historical vs current synthetic churn/fraud features; explicitly synthetic.

**Task**  
Implement PSI/KS-style feature drift checks, prediction drift, and delayed-label performance monitoring; document threshold rationale.

**Technologies**  
Python + pandas + scipy + Plotly

**Required Deliverables**  
drift module; dashboard; alert rules; baseline files.

**Acceptance Criteria**  
Drift metrics reproducible; baseline fixed/versioned; alerts include affected features and sample counts.

**Professional Skills Tested**  
Drift, monitoring, statistical process control

**Common Failure Modes**  
Alerting on every small shift; confusing drift with performance failure.

**Production Considerations**  
Trigger investigation/retraining only through policy, not automatic blind retraining.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(monitoring): add data and concept drift checks`

**Portfolio Value**  
Core MLOps competency.

---

### Day 48 — Automated Retraining Gate

**Role**  
MLOps Engineer

**Business/Technical Scenario**  
A model should retrain only when data quality and business performance justify it.

**Problem Statement**  
Implement a gated retraining workflow.

**Objective**  
Connect monitoring to lifecycle control without creating unsafe automation.

**Dataset / Data Source**  
Day 47 monitoring package + versioned training data.

**Task**  
Define eligibility checks: data freshness/quality, minimum label volume, drift, performance decline, training reproducibility, and approval gate; produce a retraining candidate artifact.

**Technologies**  
Python + MLflow + GitHub Actions

**Required Deliverables**  
retraining workflow; policy YAML; candidate model artifact; audit log.

**Acceptance Criteria**  
No automatic production promotion; all gate results stored; candidate can be rejected cleanly.

**Professional Skills Tested**  
MLOps lifecycle, governance, automation

**Common Failure Modes**  
Auto-deploying every time drift fires; ignoring data quality.

**Production Considerations**  
Add human approval and canary/shadow evaluation before promotion.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(mlops): add gated retraining workflow`

**Portfolio Value**  
Strong end-to-end lifecycle evidence.

---

### Day 49 — Canary and Rollback Simulation

**Role**  
MLOps Engineer

**Business/Technical Scenario**  
A new model is ready but its effect on live traffic is uncertain.

**Problem Statement**  
Design and simulate a safe canary release.

**Objective**  
Protect production with objective rollback signals.

**Dataset / Data Source**  
Two versioned models plus replayable prediction traffic; synthetic if necessary.

**Task**  
Replay traffic, compare champion/challenger by quality, latency, error rate, and segment health; define rollback conditions.

**Technologies**  
Python + MLflow + FastAPI + Docker

**Required Deliverables**  
canary script; metrics table; release policy; rollback demo.

**Acceptance Criteria**  
Rollback triggers are measurable and tested; challenger never silently becomes champion.

**Professional Skills Tested**  
Deployment strategy, model governance

**Common Failure Modes**  
Rollback only on aggregate metric; no segment checks.

**Production Considerations**  
Use shadow traffic or small-percentage routing before full rollout.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(deploy): simulate model canary and rollback`

**Portfolio Value**  
High-value MLOps showcase.

---

### Day 50 — Phase 4 Capstone — Full ML Lifecycle

**Role**  
MLOps Engineer / ML Engineer

**Business/Technical Scenario**  
The retention system must operate continuously, not just score once.

**Problem Statement**  
Integrate DATA → TRAIN → VALIDATE → REGISTER → DEPLOY → MONITOR → RETRAIN.

**Objective**  
Demonstrate a complete operational ML lifecycle.

**Dataset / Data Source**  
Day 35–49 artifacts + synthetic production events.

**Task**  
Wire pipeline stages, data versioning, MLflow registry, FastAPI deployment, monitoring, gated retraining, canary simulation, and rollback.

**Technologies**  
Python + DVC + MLflow + FastAPI + Docker + GitHub Actions

**Required Deliverables**  
repo; architecture; CI/CD; model registry evidence; monitoring dashboard; lifecycle runbook; demo.

**Acceptance Criteria**  
Fresh environment reproduces training; registered model serves; monitoring works; rollback demonstrated; no secrets committed.

**Professional Skills Tested**  
End-to-end MLOps, software engineering, DevOps

**Common Failure Modes**  
Point solution with no lifecycle handoff; manual undocumented deployment.

**Production Considerations**  
Map components to AWS/Azure/GCP equivalents without requiring paid infrastructure.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(capstone): ship production ml lifecycle`

**Portfolio Value**  
Capstone 2 complete and interview-ready.

---

### Day 51 — PyTorch MLP Training System

**Role**  
Deep Learning Engineer

**Business/Technical Scenario**  
A classification workload requires a neural baseline and reproducible training loop.

**Problem Statement**  
Build a clean PyTorch training system with checkpoints.

**Objective**  
Establish neural-network engineering foundations.

**Dataset / Data Source**  
DR03 Wine Quality or synthetic tabular classification; small enough for local CPU/GPU.

**Task**  
Implement Dataset/DataLoader, model, training loop, validation, checkpoint save/resume, early stopping, and metrics.

**Technologies**  
PyTorch + Python + NumPy

**Required Deliverables**  
training package; config; checkpoints; learning curves; tests.

**Acceptance Criteria**  
Resume training from checkpoint; metrics logged per epoch; deterministic seed documented.

**Professional Skills Tested**  
PyTorch, training loops, checkpointing

**Common Failure Modes**  
No validation mode; saving only final weights; shape bugs.

**Production Considerations**  
Add AMP, experiment tracking, and artifact storage.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(dl): build reproducible pytorch training loop`

**Portfolio Value**  
Demonstrates framework-level understanding.

---

### Day 52 — CNN Image Classification on MNIST

**Role**  
Computer Vision Engineer

**Business/Technical Scenario**  
An OCR workflow needs an image classifier baseline.

**Problem Statement**  
Train and evaluate a CNN with robust validation and error inspection.

**Objective**  
Go beyond a tutorial by instrumenting failures.

**Dataset / Data Source**  
DR11 MNIST; 60k train/10k test; 28×28 grayscale images.

**Task**  
Build CNN, augmentation baseline, checkpointing, confusion analysis, and misclassified-image report.

**Technologies**  
PyTorch + torchvision + matplotlib

**Required Deliverables**  
model code; test metrics; confusion matrix; misclassification gallery; README.

**Acceptance Criteria**  
Train/test separation preserved; no augmentation leakage; errors inspected by class.

**Professional Skills Tested**  
CNN, image pipelines, error analysis

**Common Failure Modes**  
Using test set for tuning; overcomplicated architecture with no benchmark.

**Production Considerations**  
Package preprocessing and inference transform together.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(cv): train and analyze cnn digit classifier`

**Portfolio Value**  
Computer-vision portfolio artifact.

---

### Day 53 — Transfer Learning for Business Image Classification

**Role**  
Computer Vision Engineer

**Business/Technical Scenario**  
A retailer wants product-category recognition with limited labeled images.

**Problem Statement**  
Use transfer learning efficiently instead of training from scratch.

**Objective**  
Compare frozen-backbone and partial fine-tuning strategies.

**Dataset / Data Source**  
Use a publicly available small image dataset from a reputable source, or a clearly synthetic/curated local dataset if access is restricted; record exact source.

**Task**  
Build dataloader, augmentations, baseline frozen backbone, fine-tune selected layers, and compare compute/performance.

**Technologies**  
PyTorch + torchvision + PIL

**Required Deliverables**  
training configs; benchmark; model checkpoint; inference demo.

**Acceptance Criteria**  
Train/validation/test separation; augmentation only on train; best checkpoint selected on validation.

**Professional Skills Tested**  
Transfer learning, computer vision, training efficiency

**Common Failure Modes**  
Fine-tuning entire network with tiny data; ignoring class imbalance.

**Production Considerations**  
Use mixed precision and model artifact versioning.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(cv): add transfer learning classifier`

**Portfolio Value**  
Professional applied CV example.

---

### Day 54 — Object Detection Systems Thinking

**Role**  
Computer Vision Engineer

**Business/Technical Scenario**  
Warehouse cameras need package-detection capability.

**Problem Statement**  
Understand and prototype an object-detection workflow without pretending a toy detector is production-ready.

**Objective**  
Design data, annotation, evaluation, and inference pipeline.

**Dataset / Data Source**  
Use COCO-format public data only if licensing/access is confirmed at implementation time; otherwise create a tiny synthetic detection dataset and label it synthetic.

**Task**  
Define bounding-box schema, train/evaluate a small detector or use a pretrained detector for inference, calculate IoU and mAP concepts, and analyze false positives.

**Technologies**  
PyTorch + torchvision/Ultralytics (one) + OpenCV

**Required Deliverables**  
dataset config; detector demo; evaluation notes; architecture diagram.

**Acceptance Criteria**  
Bounding-box coordinates validated; confidence threshold documented; evaluation method clear.

**Professional Skills Tested**  
Object detection, annotation, CV metrics

**Common Failure Modes**  
Calling accuracy mAP; ignoring NMS and class imbalance.

**Production Considerations**  
For production, address camera drift, annotation workflow, model latency, and safety constraints.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(cv): prototype warehouse object detection pipeline`

**Portfolio Value**  
Shows beyond-classification CV knowledge.

---

### Day 55 — GPU Training and Mixed Precision Benchmark

**Role**  
Deep Learning Engineer

**Business/Technical Scenario**  
Training is too slow on available hardware.

**Problem Statement**  
Measure the effect of batching, AMP, workers, and memory settings.

**Objective**  
Optimize scientifically, not by trial-and-error.

**Dataset / Data Source**  
Day 53 image dataset/model or MNIST CNN benchmark.

**Task**  
Benchmark FP32 vs AMP, batch sizes, num_workers, and gradient accumulation; track throughput, peak memory, and validation stability.

**Technologies**  
PyTorch + CUDA if available + AMP + profiling tools

**Required Deliverables**  
benchmark table; profiler output; chosen config.

**Acceptance Criteria**  
Each benchmark is repeatable enough to compare; throughput and memory both measured; accuracy impact noted.

**Professional Skills Tested**  
GPU optimization, profiling, mixed precision

**Common Failure Modes**  
Changing multiple factors at once; benchmark warm-up ignored.

**Production Considerations**  
Select deployment hardware based on cost/latency rather than habit.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`perf(dl): benchmark mixed precision training`

**Portfolio Value**  
Strong systems-level DL evidence.

---

### Day 56 — Sequence Classification with GRU

**Role**  
NLP Engineer

**Business/Technical Scenario**  
Customer messages arrive as short sequences and sentiment must be estimated.

**Problem Statement**  
Build a recurrent baseline and inspect sequence-length effects.

**Objective**  
Understand sequence modeling trade-offs before Transformers.

**Dataset / Data Source**  
DR10 GLUE/SST-2; sentiment classification benchmark.

**Task**  
Create tokenizer/vocabulary baseline or subword-compatible preprocessing, GRU classifier, padding/masking strategy, and error analysis by length.

**Technologies**  
PyTorch + Hugging Face Datasets + torchtext-like utilities

**Required Deliverables**  
model; preprocessing; evaluation; error report.

**Acceptance Criteria**  
Padding mask correct; validation protocol fixed; OOV strategy documented.

**Professional Skills Tested**  
Sequence models, masking, text preprocessing

**Common Failure Modes**  
Tokenizing before split with leakage from labels; ignoring long sequences.

**Production Considerations**  
Benchmark GRU against a Transformer later.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(nlp): add gru sentiment baseline`

**Portfolio Value**  
Clear NLP progression artifact.

---

### Day 57 — LSTM vs GRU Comparative Experiment

**Role**  
Research Engineer / NLP Engineer

**Business/Technical Scenario**  
The team wants evidence for a sequence-model choice on a constrained environment.

**Problem Statement**  
Benchmark LSTM and GRU under equal budgets.

**Objective**  
Make a model-choice recommendation tied to evidence.

**Dataset / Data Source**  
DR10 SST-2 or a similarly licensed public sentiment dataset.

**Task**  
Use matched parameter budgets where reasonable, same split, same training budget, measure quality, speed, and memory.

**Technologies**  
PyTorch + MLflow + pandas

**Required Deliverables**  
experiment report; metrics; resource benchmark.

**Acceptance Criteria**  
Comparison is controlled; no model gets an unfair tuning advantage; uncertainty discussed.

**Professional Skills Tested**  
Experimental control, sequence models, benchmarking

**Common Failure Modes**  
Comparing different preprocessing; one run only when variance is high.

**Production Considerations**  
Automate multi-seed evaluation for final decisions.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`research: compare lstm and gru under budget`

**Portfolio Value**  
Research-oriented DL artifact.

---

### Day 58 — Research Day — Reproduce a Vision Training Recipe

**Role**  
Research Engineer

**Business/Technical Scenario**  
A paper reports strong accuracy from a training recipe and augmentation strategy.

**Problem Statement**  
Reproduce a constrained subset and document deviations.

**Objective**  
Learn to distinguish architecture effects from training recipe effects.

**Dataset / Data Source**  
DR11 MNIST or a verified public image dataset.

**Task**  
Research question → cited paper → baseline → recipe implementation → controlled reproduction → error analysis → limitations.

**Technologies**  
PyTorch + MLflow + paper source

**Required Deliverables**  
reproduction notebook/script; report; configs; environment lock.

**Acceptance Criteria**  
Exact paper and dataset identified; no fabricated success claims; deviations and hardware differences recorded.

**Professional Skills Tested**  
Research methodology, reproduction, DL training

**Common Failure Modes**  
Claiming exact reproduction on different hardware without qualification.

**Production Considerations**  
Publish code and configuration sufficient for independent rerun.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`research: reproduce vision training recipe`

**Portfolio Value**  
Strong research credibility.

---

### Day 59 — Transformer Encoder for Text Classification

**Role**  
NLP Engineer

**Business/Technical Scenario**  
Support messages require more context-aware text classification than RNNs provide.

**Problem Statement**  
Build a Transformer-based classifier and understand attention behavior.

**Objective**  
Establish a practical Transformer baseline.

**Dataset / Data Source**  
DR10 SST-2 or DR08 Banking77; select one and record exact dataset revision.

**Task**  
Fine-tune a pretrained encoder; evaluate macro-F1/accuracy, latency, sequence truncation effects, and representative errors.

**Technologies**  
PyTorch + Hugging Face Transformers + Datasets

**Required Deliverables**  
fine-tuning script; model card; metrics; error analysis.

**Acceptance Criteria**  
No test-set tuning; max length justified; checkpoint reproducible.

**Professional Skills Tested**  
Transformers, fine-tuning, evaluation

**Common Failure Modes**  
Using full sequence lengths without profiling; reporting only accuracy.

**Production Considerations**  
Optimize batch inference and model serialization later.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(nlp): fine tune transformer classifier`

**Portfolio Value**  
Modern NLP engineering artifact.

---

### Day 60 — Transformer Embeddings for Semantic Similarity

**Role**  
NLP Engineer

**Business/Technical Scenario**  
Customer support wants to find semantically similar tickets.

**Problem Statement**  
Generate sentence embeddings and build a similarity search baseline.

**Objective**  
Connect representation learning to a retrieval use case.

**Dataset / Data Source**  
DR08 Banking77 or a clearly licensed support corpus; use sentence-transformers-compatible model.

**Task**  
Embed tickets, normalize vectors, evaluate similarity with labeled intent as a proxy, inspect false neighbors, and benchmark storage size.

**Technologies**  
sentence-transformers + FAISS + Python

**Required Deliverables**  
embedding job; FAISS index; retrieval demo; evaluation table.

**Acceptance Criteria**  
Index reproducible from source data; embedding model version stored; retrieval metric defined.

**Professional Skills Tested**  
Embeddings, vector search, semantic similarity

**Common Failure Modes**  
Comparing embeddings with raw cosine only without labels; stale index.

**Production Considerations**  
Add incremental indexing and metadata filters.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(search): build support ticket embedding index`

**Portfolio Value**  
Direct bridge to RAG.

---

### Day 61 — Named Entity Recognition Pipeline

**Role**  
NLP Engineer

**Business/Technical Scenario**  
An enterprise parser needs organizations, people, and locations extracted from text.

**Problem Statement**  
Build and evaluate an NER workflow.

**Objective**  
Handle token-label alignment correctly.

**Dataset / Data Source**  
DR09 CoNLL-2003; train 14,041 / validation 3,250 / test 3,453 examples; entity labels include PER/ORG/LOC/MISC.

**Task**  
Tokenize with a Transformer tokenizer, align BIO labels, fine-tune token classifier, evaluate entity-level precision/recall/F1.

**Technologies**  
Hugging Face Transformers + Datasets + seqeval/evaluate

**Required Deliverables**  
training pipeline; evaluation report; error examples.

**Acceptance Criteria**  
Label alignment unit-tested; entity-level metric used; padding ignored appropriately.

**Professional Skills Tested**  
NER, tokenization, sequence labeling

**Common Failure Modes**  
Character-level assumptions; misaligned wordpieces; token accuracy instead of entity F1.

**Production Considerations**  
Add domain-specific post-processing only as a measured component.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(nlp): fine tune transformer ner model`

**Portfolio Value**  
Strong enterprise NLP artifact.

---

### Day 62 — Research Day — Benchmark Embedding Models for Retrieval

**Role**  
Research Engineer

**Business/Technical Scenario**  
The search team must choose an embedding model for multilingual support tickets.

**Problem Statement**  
Benchmark candidate embedding models fairly.

**Objective**  
Select based on retrieval quality and resource constraints.

**Dataset / Data Source**  
DR08 Banking77 or a verified multilingual support corpus; use exact dataset/model revisions.

**Task**  
Construct query-document pairs, compare 2–4 embedding models, report Recall@k/MRR, latency, memory, and failure examples.

**Technologies**  
sentence-transformers + FAISS/Qdrant + Python

**Required Deliverables**  
benchmark harness; results CSV; report; model decision record.

**Acceptance Criteria**  
Same queries/corpus; no test leakage; ranking metrics defined; model versions pinned.

**Professional Skills Tested**  
IR evaluation, embeddings, experimental design

**Common Failure Modes**  
Using semantic similarity as a substitute for retrieval evaluation; cherry-picking queries.

**Production Considerations**  
Keep an evaluation set immutable for future regressions.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`research: benchmark embedding models for retrieval`

**Portfolio Value**  
High-value RAG preparation.

---

### Day 63 — Time-Series Forecasting with LSTM

**Role**  
Deep Learning Engineer

**Business/Technical Scenario**  
Energy demand planners want a nonlinear forecasting baseline.

**Problem Statement**  
Train a sequence model for multivariate time series and compare with classical baseline.

**Objective**  
Learn when deep forecasting is justified.

**Dataset / Data Source**  
DR16 synthetic IoT/energy-like sensor stream; explicitly synthetic; 10M+ observations generated, but prototype on a smaller rolling window.

**Task**  
Build windowed dataset, LSTM forecaster, baseline naive/ETS, time-aware split, and error analysis by horizon.

**Technologies**  
PyTorch + pandas/NumPy + statsmodels

**Required Deliverables**  
training script; forecast plots; benchmark; checkpoint.

**Acceptance Criteria**  
No leakage through scaling/window construction; baseline included; horizon-specific metrics reported.

**Professional Skills Tested**  
Deep forecasting, sequence windows, evaluation

**Common Failure Modes**  
Random split; future values in normalization statistics.

**Production Considerations**  
Use rolling retraining and resource-aware batch inference.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(forecast): add lstm demand forecasting baseline`

**Portfolio Value**  
Required deep time-series project.

---

### Day 64 — Production Debugging — GPU/Memory Failure

**Role**  
Deep Learning / MLOps Engineer

**Business/Technical Scenario**  
A training job crashes mid-epoch with out-of-memory errors after a data refresh.

**Problem Statement**  
Identify the change causing memory growth and implement a robust fix.

**Objective**  
Practice profiling and resource-aware debugging.

**Dataset / Data Source**  
Day 63 code plus synthetic configuration that increases sequence length/batch size.

**Task**  
Profile memory by batch, inspect data loader/pinning/caching, reduce peak memory via accumulation/AMP/chunking, and validate throughput.

**Technologies**  
PyTorch + profiler + Python + Docker

**Required Deliverables**  
incident report; profiler evidence; fix; regression benchmark.

**Acceptance Criteria**  
Peak memory decreases materially; training remains numerically stable; root cause isolated.

**Professional Skills Tested**  
GPU debugging, profiling, training stability

**Common Failure Modes**  
Blindly decreasing batch size; ignoring throughput trade-off.

**Production Considerations**  
Set resource limits, observability, and automated smoke tests for training jobs.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`fix(dl): resolve training memory regression`

**Portfolio Value**  
Production-grade deep-learning troubleshooting.

---

### Day 65 — Phase 5 Capstone — Intelligent Document Classifier

**Role**  
DL/NLP Engineer

**Business/Technical Scenario**  
A document-processing workflow needs image/text classification with confidence scoring.

**Problem Statement**  
Combine transfer learning or Transformer classification, inference, and error analysis into one application.

**Objective**  
Ship a practical deep-learning service component.

**Dataset / Data Source**  
Use DR10/DR09 for NLP variant or a verified public image dataset for CV; exact source recorded.

**Task**  
Build training pipeline, checkpointing, evaluation, confidence analysis, inference CLI/API, and model card.

**Technologies**  
PyTorch + Transformers/torchvision + FastAPI + Docker

**Required Deliverables**  
repo; model; inference API; tests; model card; demo.

**Acceptance Criteria**  
Reproducible training/inference; performance baseline; confidence calibration note; container runs.

**Professional Skills Tested**  
Deep learning, API, packaging, evaluation

**Common Failure Modes**  
Notebook-only project; no error analysis; no reproducible checkpoint.

**Production Considerations**  
Add async/batch inference and model observability.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(capstone): ship document intelligence classifier`

**Portfolio Value**  
Capstone 3: Deep Learning Application.

---

### Day 66 — LLM Application Architecture and Model Selection

**Role**  
AI Engineer

**Business/Technical Scenario**  
A company wants an internal assistant but has uncertain model, cost, and latency constraints.

**Problem Statement**  
Design a provider-independent LLM architecture and selection matrix.

**Objective**  
Choose models from requirements, not hype.

**Dataset / Data Source**  
Synthetic Support Tickets DR15 plus a small curated prompt/eval set.

**Task**  
Define task taxonomy, quality rubric, latency/cost assumptions, model interface abstraction, fallback strategy, and evaluation dataset.

**Technologies**  
Python + provider SDK abstraction + Pydantic

**Required Deliverables**  
architecture diagram; model adapter interface; eval dataset; decision matrix.

**Acceptance Criteria**  
At least two interchangeable model adapters; prompt inputs/outputs structured; no provider lock-in in business logic.

**Professional Skills Tested**  
LLM architecture, model selection, evaluation framing

**Common Failure Modes**  
Calling one API directly throughout the codebase; no evaluation set.

**Production Considerations**  
Add policy/routing layer and per-model cost telemetry.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(genai): add provider independent llm interface`

**Portfolio Value**  
Strong GenAI systems-design artifact.

---

### Day 67 — Structured Prompting with JSON Schemas

**Role**  
AI Engineer

**Business/Technical Scenario**  
Support operations needs machine-readable ticket triage outputs.

**Problem Statement**  
Generate validated structured data from free text.

**Objective**  
Make LLM output safe for downstream automation.

**Dataset / Data Source**  
DR15 synthetic support tickets.

**Task**  
Define Pydantic schema, system prompt, few-shot examples, parse/validate/retry logic, and adversarial test cases.

**Technologies**  
Python + LLM API + Pydantic

**Required Deliverables**  
prompt spec; schema; parser; tests; sample outputs.

**Acceptance Criteria**  
Invalid JSON is rejected/retried; required fields guaranteed after validation; adversarial inputs tested.

**Professional Skills Tested**  
Prompt engineering, structured outputs, validation

**Common Failure Modes**  
Trusting free-form output; prompt injection through ticket text.

**Production Considerations**  
Use API-native structured output/tool calling where supported and still validate server-side.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(genai): add schema validated ticket triage`

**Portfolio Value**  
Practical enterprise GenAI artifact.

---

### Day 68 — Tool Calling for Order Support

**Role**  
AI Engineer

**Business/Technical Scenario**  
An assistant must look up order status rather than invent it.

**Problem Statement**  
Build a tool-using workflow with strict tool schemas.

**Objective**  
Ground actions in real data.

**Dataset / Data Source**  
Synthetic order database; explicitly synthetic; SQLite/PostgreSQL.

**Task**  
Implement get_order_status, search_customer_orders, and create_support_case as mock tools; enforce authorization context and audit log.

**Technologies**  
Python + FastAPI/Flask + LLM function/tool calling + SQLAlchemy

**Required Deliverables**  
tool registry; schemas; mock DB; audit log; tests.

**Acceptance Criteria**  
Assistant cannot execute undefined tools; tool args validated; unauthorized customer access blocked.

**Professional Skills Tested**  
Tool calling, backend integration, auth context

**Common Failure Modes**  
Letting model choose raw SQL; missing tenant checks.

**Production Considerations**  
Replace mocks with production APIs behind an allowlisted tool layer.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(agent): add tool calling for order support`

**Portfolio Value**  
Shows agent-system thinking.

---

### Day 69 — Hallucination Reduction with Grounding and Abstention

**Role**  
AI Engineer

**Business/Technical Scenario**  
A customer-facing assistant invents policies when documents are missing.

**Problem Statement**  
Implement answer-with-evidence plus abstention behavior.

**Objective**  
Reduce unsupported claims without pretending hallucinations are solved.

**Dataset / Data Source**  
Synthetic support-policy corpus; explicitly synthetic; 200–500 short policy documents.

**Task**  
Build prompt policy, retrieval-grounded answering, confidence/evidence checks, and 'cannot verify' responses for unsupported questions.

**Technologies**  
Python + LLM API + embeddings + FAISS/Chroma

**Required Deliverables**  
grounded QA app; evaluation set; hallucination error log.

**Acceptance Criteria**  
Unsupported-answer rate measured on a fixed set; citations/evidence required; abstention cases documented.

**Professional Skills Tested**  
Grounding, evaluation, prompt design

**Common Failure Modes**  
Using model confidence as truth; citations without evidence.

**Production Considerations**  
Add automated faithfulness checks and human review for high-impact domains.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(genai): add grounded answer and abstention policy`

**Portfolio Value**  
Good reliability-focused GenAI artifact.

---

### Day 70 — Research Day — LLM Prompt Evaluation Harness

**Role**  
Research Engineer / AI Engineer

**Business/Technical Scenario**  
Prompt changes are judged subjectively by developers.

**Problem Statement**  
Create a repeatable evaluation harness for prompt variants.

**Objective**  
Turn prompt engineering into measurable experimentation.

**Dataset / Data Source**  
DR15 synthetic support tickets; 100–500 fixed evaluation cases.

**Task**  
Define criteria: correctness, schema validity, refusal behavior, grounding, verbosity, and cost; compare 3 prompt variants with paired evaluation.

**Technologies**  
Python + LLM API + pandas + evaluation framework of choice

**Required Deliverables**  
eval dataset; harness; scorecard; prompt decision record.

**Acceptance Criteria**  
Same cases across prompts; rubric versioned; failures stored; costs measured; no fabricated evaluator claims.

**Professional Skills Tested**  
LLM evals, experimentation, cost analysis

**Common Failure Modes**  
Changing eval cases per prompt; relying only on an LLM judge without checks.

**Production Considerations**  
Add human calibration set and regression tests in CI.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`research: build llm prompt evaluation harness`

**Portfolio Value**  
High-value GenAI research artifact.

---

### Day 71 — Streaming LLM Response API

**Role**  
AI Engineer

**Business/Technical Scenario**  
A chat UI feels slow because users wait for full completion.

**Problem Statement**  
Implement token-streaming over HTTP while preserving error handling.

**Objective**  
Improve perceived latency without sacrificing safety.

**Dataset / Data Source**  
DR15 support prompts; no new dataset required.

**Task**  
Create streaming endpoint, cancellation handling, timeout policy, request IDs, and partial-output logging without storing secrets.

**Technologies**  
FastAPI + SSE/WebSocket + provider SDK

**Required Deliverables**  
streaming API; frontend demo; load test; logs.

**Acceptance Criteria**  
First-token latency measured; cancellation works; malformed events handled; request tracing present.

**Professional Skills Tested**  
Streaming APIs, async Python, observability

**Common Failure Modes**  
Blocking synchronous call; buffering entire answer before send.

**Production Considerations**  
Add backpressure, connection limits, and moderation hooks.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(api): stream llm responses over sse`

**Portfolio Value**  
Production-style AI API artifact.

---

### Day 72 — Multimodal Document Extraction

**Role**  
AI Engineer

**Business/Technical Scenario**  
Operations receives invoices as scans and needs structured fields.

**Problem Statement**  
Build a multimodal extraction workflow with validation.

**Objective**  
Combine image/document understanding with structured output.

**Dataset / Data Source**  
Use a small set of publicly licensed sample invoices or synthetic invoice images; synthetic samples must be labeled.

**Task**  
Extract vendor/date/total/line-item fields, validate totals, preserve source references, and route low-confidence cases to review.

**Technologies**  
Python + multimodal LLM API + OpenCV/PIL + Pydantic

**Required Deliverables**  
document pipeline; sample JSON; validation rules; review queue demo.

**Acceptance Criteria**  
Field schema validated; arithmetic checks implemented; low-confidence outputs are reviewable rather than silently accepted.

**Professional Skills Tested**  
Multimodal AI, document intelligence, validation

**Common Failure Modes**  
Trusting OCR/LLM blindly; no provenance.

**Production Considerations**  
Add encrypted storage, PII controls, retention policy, and human-in-the-loop approval.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(multimodal): build invoice extraction workflow`

**Portfolio Value**  
Strong enterprise AI use case.

---

### Day 73 — Production Debugging — LLM Cost Spike

**Role**  
AI Platform Engineer

**Business/Technical Scenario**  
A prompt update doubles token usage and monthly spend.

**Problem Statement**  
Diagnose token-growth and latency regressions and mitigate them.

**Objective**  
Treat cost as an engineering metric.

**Dataset / Data Source**  
Synthetic request log with prompt/version/token/latency metadata.

**Task**  
Analyze token distribution, identify prompt bloat/history growth, implement context trimming/summarization/caching where appropriate, and compare before/after cost.

**Technologies**  
Python + pandas + LLM API logs

**Required Deliverables**  
cost analysis; patched prompt/context policy; benchmark.

**Acceptance Criteria**  
Token and cost metrics reconcile; p95 latency does not regress materially; quality regression suite passes.

**Professional Skills Tested**  
Cost optimization, observability, context management

**Common Failure Modes**  
Compressing prompts without evaluation; hiding cost in a vendor bill.

**Production Considerations**  
Add per-user quotas, budget alerts, model routing, and cache metrics.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`fix(ai): resolve llm token and cost regression`

**Portfolio Value**  
Rare and valuable production AI skill.

---

### Day 74 — AI Agent with Bounded Toolset

**Role**  
AI Engineer

**Business/Technical Scenario**  
Customer operations wants a semi-autonomous assistant for support workflows.

**Problem Statement**  
Build an agent that can reason over a small set of safe tools.

**Objective**  
Constrain autonomy through explicit policies.

**Dataset / Data Source**  
Synthetic support/order DB + DR15 tickets.

**Task**  
Implement plan→tool→observe loop with max steps, allowlisted tools, validation, timeout, audit log, and human handoff.

**Technologies**  
Python + tool-calling LLM + SQLAlchemy + FastAPI

**Required Deliverables**  
agent service; tool schemas; policy config; test suite; trace samples.

**Acceptance Criteria**  
Agent stops after max steps; unsafe actions require approval; every tool call logged; unauthorized data access blocked.

**Professional Skills Tested**  
Agents, orchestration, safety, observability

**Common Failure Modes**  
Infinite loops; model-generated SQL; hidden state.

**Production Considerations**  
Add policy engine, tool scopes, and replayable traces.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(agent): build bounded support operations agent`

**Portfolio Value**  
Demonstrates agent engineering rather than chatbot prompting.

---

### Day 75 — Function-Calling Evaluation and Regression Suite

**Role**  
AI Engineer / QA Engineer

**Business/Technical Scenario**  
The agent works, but a prompt/model upgrade breaks tool selection.

**Problem Statement**  
Build a regression suite for tool-call correctness.

**Objective**  
Test behavioral contracts, not only text similarity.

**Dataset / Data Source**  
Synthetic support/order scenarios; 200+ test cases target.

**Task**  
Evaluate tool selection accuracy, argument validity, authorization, final-answer grounding, and failure behavior across model versions.

**Technologies**  
Python + pytest + LLM API + structured logs

**Required Deliverables**  
regression dataset; pytest suite; score report; CI job.

**Acceptance Criteria**  
Tests cover success/error/ambiguous/unauthorized cases; failures store traces; threshold gates are defined.

**Professional Skills Tested**  
AI QA, behavioral testing, agents

**Common Failure Modes**  
Only snapshot-testing final prose; no negative tests.

**Production Considerations**  
Run a small regression suite on every PR and a larger suite nightly.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`test(agent): add tool calling regression suite`

**Portfolio Value**  
High-value AI quality engineering artifact.

---

### Day 76 — Research Day — LLM Model Benchmark Under Cost Constraint

**Role**  
Research Engineer

**Business/Technical Scenario**  
Product needs a model recommendation for support automation under a fixed monthly budget.

**Problem Statement**  
Benchmark multiple available models against quality, latency, and cost.

**Objective**  
Make model selection evidence-based and repeatable.

**Dataset / Data Source**  
DR15 fixed evaluation set; use current provider/model documentation at implementation time.

**Task**  
Run same prompts and tools across 2–4 model options; compare task success, schema validity, safety failures, p95 latency, and estimated cost.

**Technologies**  
Python + provider SDKs + pandas

**Required Deliverables**  
benchmark harness; results; model selection report; limitations.

**Acceptance Criteria**  
Model names/versions and pricing sources captured on run date; no fabricated costs/results; test cases fixed.

**Professional Skills Tested**  
Benchmarking, model routing, cost engineering

**Common Failure Modes**  
Comparing different prompt variants; stale pricing assumptions.

**Production Considerations**  
Add routing rules based on task complexity and confidence.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`research: benchmark llm models for support tasks`

**Portfolio Value**  
Excellent GenAI decision artifact.

---

### Day 77 — Context Management and Conversation Memory

**Role**  
AI Engineer

**Business/Technical Scenario**  
Long-running chats become expensive and drift away from current user intent.

**Problem Statement**  
Design bounded conversational memory.

**Objective**  
Keep useful context while limiting token growth.

**Dataset / Data Source**  
Synthetic support conversations, explicitly synthetic; long multi-turn sessions.

**Task**  
Implement short-term window, summarized memory, user/profile memory boundaries, and retrieval of relevant past turns; compare token usage and answer quality.

**Technologies**  
Python + LLM API + vector store optional

**Required Deliverables**  
memory module; benchmark; policy document; tests.

**Acceptance Criteria**  
No cross-user memory leakage; token budget bounded; stale-memory test cases included.

**Professional Skills Tested**  
Context management, privacy, cost optimization

**Common Failure Modes**  
Sending entire chat forever; storing sensitive data indefinitely.

**Production Considerations**  
Add retention TTL, encryption, tenant isolation, and delete workflows.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(agent): add bounded conversational memory`

**Portfolio Value**  
Important production-agent competency.

---

### Day 78 — AI API Reliability: Retries, Timeouts, Fallbacks

**Role**  
AI Platform Engineer

**Business/Technical Scenario**  
A provider experiences intermittent 429/5xx errors.

**Problem Statement**  
Build resilient provider integration.

**Objective**  
Fail gracefully and avoid retry storms.

**Dataset / Data Source**  
Synthetic fault-injection wrapper around provider client.

**Task**  
Implement timeout, exponential backoff with jitter, bounded retries, circuit-breaker behavior, provider fallback, and request IDs.

**Technologies**  
Python + httpx + FastAPI

**Required Deliverables**  
provider client; fault tests; metrics; runbook.

**Acceptance Criteria**  
Retries bounded; 429 respects backoff semantics; no duplicate side effects for non-idempotent tools; fallback behavior tested.

**Professional Skills Tested**  
Reliability engineering, distributed systems

**Common Failure Modes**  
Infinite retries; retrying unsafe writes.

**Production Considerations**  
Add provider routing based on health/cost and graceful degradation modes.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(reliability): harden llm provider client`

**Portfolio Value**  
Strong AI platform engineering artifact.

---

### Day 79 — Enterprise AI Access Control

**Role**  
AI Security Engineer

**Business/Technical Scenario**  
Different employees can access different documents and tools.

**Problem Statement**  
Implement tenant-aware authorization in an AI application.

**Objective**  
Prevent data leakage through retrieval and tools.

**Dataset / Data Source**  
Synthetic multi-tenant documents/orders; explicitly synthetic.

**Task**  
Create RBAC/ABAC policy, tenant IDs, document ACLs, tool permissions, and tests attempting cross-tenant access.

**Technologies**  
FastAPI + PostgreSQL + SQLAlchemy + Pydantic

**Required Deliverables**  
auth middleware; policy tables; security tests; threat model.

**Acceptance Criteria**  
Cross-tenant reads blocked; unauthorized tools rejected; audit log records principal and action.

**Professional Skills Tested**  
Authorization, tenant isolation, secure AI design

**Common Failure Modes**  
Filtering only in prompt; trusting model to respect ACLs.

**Production Considerations**  
Enforce access at data/tool layer and test continuously.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(security): enforce tenant aware ai authorization`

**Portfolio Value**  
High-signal enterprise security artifact.

---

### Day 80 — Phase 6 Capstone — Production Generative AI Assistant

**Role**  
AI Engineer

**Business/Technical Scenario**  
A customer-support organization wants a reliable assistant for triage, order lookup, and draft responses.

**Problem Statement**  
Integrate prompting, structured outputs, tools, streaming, reliability, safety, memory, and evaluation.

**Objective**  
Deliver a production-shaped GenAI application.

**Dataset / Data Source**  
DR15 synthetic tickets + synthetic order DB + policy docs.

**Task**  
Build web/API service with tool calling, schemas, streaming, bounded memory, retries, access control, eval suite, cost telemetry, and human handoff.

**Technologies**  
Python + FastAPI + PostgreSQL/SQLite + LLM APIs + Docker

**Required Deliverables**  
full repo; architecture; tests; eval report; security test report; Docker; demo.

**Acceptance Criteria**  
Regression suite passes; cross-tenant attacks blocked; latency/cost metrics documented; fallback works; secrets externalized.

**Professional Skills Tested**  
GenAI engineering, agents, security, reliability

**Common Failure Modes**  
Chatbot-only architecture; no eval; no tool permissions.

**Production Considerations**  
Prepare RAG integration next and wire monitoring/CI.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(capstone): ship production generative ai assistant`

**Portfolio Value**  
Capstone 4: Generative AI Application.

---

### Day 81 — RAG Ingestion Pipeline for Enterprise PDFs

**Role**  
RAG Engineer

**Business/Technical Scenario**  
Employees need answers from policies and procedures stored as PDFs.

**Problem Statement**  
Build reliable document ingestion with metadata and version tracking.

**Objective**  
Create the foundation for retrieval, not just a chatbot.

**Dataset / Data Source**  
Use synthetic policy PDFs or a small public document collection with verified rights; synthetic recommended for private-style content.

**Task**  
Extract text, normalize, chunk with metadata, assign document/version IDs, and create an index manifest.

**Technologies**  
Python + PyMuPDF/pypdf + sentence-transformers + FAISS/Chroma

**Required Deliverables**  
ingestion package; chunks parquet/JSONL; manifest; sample index.

**Acceptance Criteria**  
Document IDs/version IDs retained; chunk boundaries reproducible; empty/failed documents quarantined.

**Professional Skills Tested**  
PDF processing, chunking, metadata, indexing

**Common Failure Modes**  
Overlapping chunks without measuring; dropping page numbers/source references.

**Production Considerations**  
Use object storage and incremental re-indexing on changed documents.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(rag): build versioned pdf ingestion pipeline`

**Portfolio Value**  
Core RAG engineering foundation.

---

### Day 82 — Semantic Retrieval Baseline with Vector Search

**Role**  
RAG Engineer

**Business/Technical Scenario**  
Users ask natural-language questions over the policy corpus.

**Problem Statement**  
Implement top-k semantic retrieval.

**Objective**  
Measure retrieval quality before adding LLM generation.

**Dataset / Data Source**  
Day 81 chunked policy corpus + 100–300 synthetic queries with expected source IDs.

**Task**  
Embed chunks, build vector index, retrieve top-k, and measure Recall@k/Precision@k against labeled relevance.

**Technologies**  
Python + sentence-transformers + FAISS/Chroma

**Required Deliverables**  
retriever; evaluation dataset; metrics report; demo.

**Acceptance Criteria**  
Evaluation queries fixed; embedding/index version logged; retrieval metrics reported for multiple k values.

**Professional Skills Tested**  
IR evaluation, embeddings, vector search

**Common Failure Modes**  
Evaluating answer quality before retrieval quality; index built from test docs with leakage.

**Production Considerations**  
Add incremental updates and metadata filtering.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(rag): add semantic policy retriever`

**Portfolio Value**  
Important retrieval-specific artifact.

---

### Day 83 — Hybrid Retrieval with BM25 + Vector Search

**Role**  
RAG Engineer

**Business/Technical Scenario**  
Exact policy codes and semantic paraphrases must both retrieve correctly.

**Problem Statement**  
Combine lexical and semantic retrieval.

**Objective**  
Improve robustness to exact-match and conceptual queries.

**Dataset / Data Source**  
Day 81 corpus + fixed evaluation set.

**Task**  
Implement BM25, dense retrieval, rank fusion, and compare against dense-only baseline.

**Technologies**  
Python + BM25 implementation + FAISS/Chroma + pandas

**Required Deliverables**  
hybrid retriever; benchmark; fusion config.

**Acceptance Criteria**  
Hybrid retrieval improves or selectively helps defined query categories; fusion method documented.

**Professional Skills Tested**  
Hybrid search, ranking, evaluation

**Common Failure Modes**  
Assuming dense embeddings solve exact identifiers; uncalibrated score fusion.

**Production Considerations**  
Add learned or normalized fusion and query-type routing.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(rag): add hybrid lexical semantic retrieval`

**Portfolio Value**  
Strong practical RAG skill.

---

### Day 84 — Research Day — Reranking Experiment

**Role**  
Research Engineer / RAG Engineer

**Business/Technical Scenario**  
Top-k retrieval contains relevant passages but ranking is weak.

**Problem Statement**  
Test a reranker on a fixed candidate set.

**Objective**  
Measure whether reranking adds useful signal relative to cost.

**Dataset / Data Source**  
Day 83 corpus + fixed relevance-labeled query set; use a verified reranker/model source.

**Task**  
Compare no reranking vs cross-encoder reranking; measure nDCG@k/MRR/Recall and latency.

**Technologies**  
Python + sentence-transformers or Hugging Face reranker + FAISS

**Required Deliverables**  
research report; latency-quality curve; configs.

**Acceptance Criteria**  
Candidate set identical across conditions; query set fixed; model/version captured.

**Professional Skills Tested**  
Reranking, IR research, latency trade-offs

**Common Failure Modes**  
Changing candidate count and reranker simultaneously.

**Production Considerations**  
Use reranking only when lift justifies p95 latency/cost.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`research: evaluate reranking for enterprise search`

**Portfolio Value**  
Research + production trade-off artifact.

---

### Day 85 — RAG Generation with Citations

**Role**  
AI Engineer / RAG Engineer

**Business/Technical Scenario**  
Policy answers must point users to source sections.

**Problem Statement**  
Generate grounded answers with citations to retrieved chunks.

**Objective**  
Make provenance part of the output contract.

**Dataset / Data Source**  
Day 81–84 policy corpus and fixed query set.

**Task**  
Create retrieval→prompt→generation pipeline with citation IDs, source snippets, abstention, and evidence validation.

**Technologies**  
Python + LLM API + vector search + Pydantic

**Required Deliverables**  
RAG API; citation renderer; evaluation script; sample answers.

**Acceptance Criteria**  
Every non-abstained answer cites at least one retrieved source; cited chunk actually supports the claim on evaluation set.

**Professional Skills Tested**  
Grounded generation, citations, prompt design

**Common Failure Modes**  
Citation fabrication; prompt contains sources but model cites wrong IDs.

**Production Considerations**  
Store source hashes and document versions in answers for auditability.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(rag): add grounded answers with citations`

**Portfolio Value**  
Direct portfolio-ready RAG feature.

---

### Day 86 — Query Rewriting and Multi-Query Retrieval

**Role**  
RAG Engineer

**Business/Technical Scenario**  
Users ask vague follow-up questions and retrieval misses important documents.

**Problem Statement**  
Improve recall using query rewriting and multiple retrieval queries.

**Objective**  
Measure lift and control extra latency.

**Dataset / Data Source**  
Day 85 evaluation set with conversational queries.

**Task**  
Implement standalone-question rewrite, 2–4 alternate queries, retrieve/merge/deduplicate, then rerank; compare to single-query baseline.

**Technologies**  
Python + LLM API + FAISS/Chroma + reranker

**Required Deliverables**  
retrieval workflow; evaluation; latency analysis.

**Acceptance Criteria**  
Recall@k improves on targeted cases without uncontrolled token/latency growth; rewritten queries logged.

**Professional Skills Tested**  
Query expansion, retrieval orchestration, latency control

**Common Failure Modes**  
Generating too many queries; losing original intent.

**Production Considerations**  
Use adaptive rewriting only when first-pass retrieval confidence is low.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(rag): add adaptive multi query retrieval`

**Portfolio Value**  
Advanced retrieval engineering.

---

### Day 87 — Production Debugging — RAG Retrieval Drift

**Role**  
RAG Engineer / MLOps Engineer

**Business/Technical Scenario**  
New documents were added and the assistant now retrieves obsolete policy versions.

**Problem Statement**  
Diagnose stale indexes, metadata bugs, or embedding drift.

**Objective**  
Recover correct document-version behavior.

**Dataset / Data Source**  
Synthetic versioned policy corpus with injected stale-index defect.

**Task**  
Inspect index manifest, document/version metadata, changed-file detection, and retrieval samples; rebuild only affected records.

**Technologies**  
Python + vector DB + SQL metadata + logs

**Required Deliverables**  
incident report; index repair; regression tests; monitoring metric.

**Acceptance Criteria**  
Obsolete versions excluded according to policy; unaffected docs remain indexed; repair idempotent.

**Professional Skills Tested**  
Index lifecycle, debugging, metadata correctness

**Common Failure Modes**  
Full reindex without root-cause analysis; relying on timestamps only.

**Production Considerations**  
Build automatic freshness checks and document-level reindex queues.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`fix(rag): repair stale policy retrieval index`

**Portfolio Value**  
Strong production RAG troubleshooting.

---

### Day 88 — Conversational RAG with Access Control

**Role**  
RAG Engineer / Security Engineer

**Business/Technical Scenario**  
Employees ask follow-up questions over documents they are authorized to see.

**Problem Statement**  
Combine conversation state with document-level ACL filtering.

**Objective**  
Prevent memory and retrieval from crossing user permissions.

**Dataset / Data Source**  
Synthetic multi-tenant policy corpus; explicit tenant/user/role metadata.

**Task**  
Implement conversation-aware retrieval, query rewrite, ACL filter at retrieval layer, grounded answer, and cross-tenant attack tests.

**Technologies**  
FastAPI + PostgreSQL + Qdrant/Chroma + LLM API

**Required Deliverables**  
service; ACL middleware; retrieval tests; threat model.

**Acceptance Criteria**  
Unauthorized documents never enter retrieved context; prompts do not perform authorization.

**Professional Skills Tested**  
Secure RAG, conversational state, authorization

**Common Failure Modes**  
Filtering after retrieval; tenant ID omitted from vector metadata.

**Production Considerations**  
Audit every retrieval decision and support permission-change reindex/filter semantics.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(security): secure conversational rag retrieval`

**Portfolio Value**  
Advanced enterprise RAG portfolio item.

---

### Day 89 — Research Day — RAG Evaluation and Hallucination Measurement

**Role**  
Research Engineer

**Business/Technical Scenario**  
Leadership wants evidence that the RAG system is improving answer reliability.

**Problem Statement**  
Build an evaluation protocol that separates retrieval failures from generation failures.

**Objective**  
Measure retrieval recall, groundedness, answer correctness, and abstention behavior.

**Dataset / Data Source**  
Fixed RAG evaluation set with source-of-truth answers and relevant chunk IDs; synthetic policy corpus.

**Task**  
Create baseline→retrieval ablation→generation comparison; categorize hallucinations, unsupported claims, and retrieval misses; report confidence intervals where appropriate.

**Technologies**  
Python + pandas + evaluation framework + LLM API

**Required Deliverables**  
RAG research report; error taxonomy; score dashboard; regression dataset.

**Acceptance Criteria**  
Retrieval and generation metrics separated; judge rubric versioned; manually reviewed calibration sample included.

**Professional Skills Tested**  
RAG evaluation, scientific analysis, hallucination measurement

**Common Failure Modes**  
Single scalar 'RAG score'; judge bias ignored.

**Production Considerations**  
Use the suite as a release gate and monitor slices by query type.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`research: build rag reliability evaluation suite`

**Portfolio Value**  
High-value RAG research artifact.

---

### Day 90 — Phase 7 Capstone — Production Enterprise RAG

**Role**  
RAG Engineer / AI Engineer

**Business/Technical Scenario**  
A company needs a secure internal knowledge assistant for versioned policies.

**Problem Statement**  
Integrate ingestion, retrieval, hybrid search, reranking, citations, conversation, ACLs, updates, and evaluation.

**Objective**  
Deliver a portfolio-quality RAG system with operational controls.

**Dataset / Data Source**  
Synthetic enterprise policy corpus + optional public docs with verified rights.

**Task**  
Build full ingestion/index/update pipeline, hybrid retrieval, reranking, grounded generation, conversational RAG, access control, evaluation, monitoring, and versioning.

**Technologies**  
Python + FastAPI + PostgreSQL/pgvector or Qdrant + LLM API + Docker

**Required Deliverables**  
full repo; architecture; ingestion CLI; API; tests; eval report; security report; demo.

**Acceptance Criteria**  
Fresh build reproduces index; updates affect only changed docs; ACL tests pass; citation/eval gates pass; Docker runs.

**Professional Skills Tested**  
RAG architecture, security, evaluation, operations

**Common Failure Modes**  
LLM-first project with weak retrieval; stale docs; no ACL enforcement.

**Production Considerations**  
Add production tracing, autoscaling, disaster recovery, and provider-independent model adapters.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(capstone): ship secure enterprise rag platform`

**Portfolio Value**  
Capstone 5: Production RAG System.

---

### Day 91 — Cloud Deployment Architecture Mapping

**Role**  
Cloud / MLOps Engineer

**Business/Technical Scenario**  
The team wants a cloud-ready architecture but no paid commitment yet.

**Problem Statement**  
Map the local system to AWS, Azure, and Google Cloud primitives.

**Objective**  
Demonstrate cloud literacy without requiring expensive infrastructure.

**Dataset / Data Source**  
Day 90 system architecture.

**Task**  
Create three mapping diagrams: object storage, managed Postgres/vector DB options, container hosting, secrets, observability, CI/CD, and scheduled jobs; preserve a local free-tier path.

**Technologies**  
Docker + GitHub Actions + AWS/Azure/GCP service concepts

**Required Deliverables**  
architecture diagrams; cost-control notes; deployment matrix.

**Acceptance Criteria**  
Every major component has a local alternative and at least one cloud mapping; no expensive service is mandatory for the challenge.

**Professional Skills Tested**  
Cloud architecture, cost awareness, deployment design

**Common Failure Modes**  
Picking services without workload reasoning; ignoring egress/managed-service costs.

**Production Considerations**  
Add IaC only for a small demonstrator when it helps, with budget guardrails.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`docs(cloud): map ai platform to aws azure gcp`

**Portfolio Value**  
Cloud-readiness portfolio artifact.

---

### Day 92 — Research Day — Retrieval vs Fine-Tuning Decision Study

**Role**  
Research Engineer

**Business/Technical Scenario**  
The product team asks whether to fine-tune an LLM or improve retrieval/prompting.

**Problem Statement**  
Run a controlled study comparing retrieval/prompt improvements against a lightweight fine-tuning baseline where feasible.

**Objective**  
Make a defensible architecture choice.

**Dataset / Data Source**  
DR15 support corpus + fixed evaluation set; use provider/open-source model depending on local compute; document constraints.

**Task**  
Define baseline, improved retrieval, prompt optimization, and fine-tuning/adapter condition; compare quality, cost, latency, data requirements, and maintenance.

**Technologies**  
Python + Transformers/PEFT or provider fine-tuning if available + RAG stack

**Required Deliverables**  
decision report; experiment matrix; cost/latency table; limitations.

**Acceptance Criteria**  
No cherry-picking; evaluation fixed; training data separated; costs/assumptions sourced and dated.

**Professional Skills Tested**  
Research design, LLM adaptation, architecture decisions

**Common Failure Modes**  
Fine-tuning a model without sufficient data; claiming general superiority from one task.

**Production Considerations**  
Choose architecture based on observed bottleneck and maintenance burden.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`research: compare retrieval and adaptation strategies`

**Portfolio Value**  
Excellent senior-level GenAI decision artifact.

---

### Day 93 — Production Debugging — CI/CD Failure Drill

**Role**  
DevOps / MLOps Engineer

**Business/Technical Scenario**  
A release pipeline suddenly fails after a dependency update.

**Problem Statement**  
Diagnose the failure and restore the pipeline safely.

**Objective**  
Practice root-cause analysis for delivery systems.

**Dataset / Data Source**  
Repository fixture with intentionally broken dependency/workflow assumption.

**Task**  
Inspect workflow logs, dependency graph, lockfile changes, Python/runtime matrix, and Docker build; patch with the smallest safe change and add a regression guard.

**Technologies**  
GitHub Actions + Python + Docker + dependency tools

**Required Deliverables**  
incident report; fix PR-style commit; workflow test; rollback notes.

**Acceptance Criteria**  
Failure cause identified from logs; fix reproducible; pipeline green; update pinned dependencies or matrix as justified.

**Professional Skills Tested**  
CI/CD debugging, dependency management

**Common Failure Modes**  
Rerunning until it passes; unpinned rollback.

**Production Considerations**  
Use Dependabot/Renovate-style updates, staged upgrades, and artifact provenance.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`fix(ci): resolve release pipeline dependency failure`

**Portfolio Value**  
Practical DevOps evidence.

---

### Day 94 — AI Security Threat Model and Red-Team Test Suite

**Role**  
AI Security Engineer

**Business/Technical Scenario**  
The enterprise AI platform may face prompt injection and malicious documents.

**Problem Statement**  
Develop defensive security tests and mitigations.

**Objective**  
Turn known threats into executable controls.

**Dataset / Data Source**  
Day 90 RAG + agent system; synthetic malicious documents/prompts.

**Task**  
Model threats for prompt injection, data exfiltration, tool abuse, insecure RAG, PII leakage, auth bypass, rate abuse; implement safe tests and mitigations.

**Technologies**  
Python + pytest + FastAPI + RAG/agent stack

**Required Deliverables**  
threat model; security test suite; mitigation report; severity matrix.

**Acceptance Criteria**  
Tests demonstrate blocked/contained cases; no exploit instructions are required; controls enforced outside the model.

**Professional Skills Tested**  
AI security, threat modeling, auth, input/output validation

**Common Failure Modes**  
Relying on system prompts as security boundary; no rate limits.

**Production Considerations**  
Add continuous red-team regression suite, secret scanning, dependency scanning, and least-privilege tools.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`test(security): add ai threat and abuse regression suite`

**Portfolio Value**  
High-value enterprise security signal.

---

### Day 95 — Observability: Logs, Traces, Metrics for AI

**Role**  
AI Platform / MLOps Engineer

**Business/Technical Scenario**  
Incidents require tracing a user request through retrieval, tools, model calls, and response.

**Problem Statement**  
Implement end-to-end observability without logging sensitive content indiscriminately.

**Objective**  
Make system behavior diagnosable.

**Dataset / Data Source**  
Day 90 platform plus synthetic traces.

**Task**  
Add request ID, stage timing, retrieval top-k IDs, tool calls, model latency/token metrics, errors, and privacy-aware sampling.

**Technologies**  
Python + OpenTelemetry concepts + structured JSON logs + Prometheus concepts

**Required Deliverables**  
telemetry module; dashboard; example trace; privacy logging policy.

**Acceptance Criteria**  
Every request has correlation ID; p95 stage timing available; secrets/PII not logged by default.

**Professional Skills Tested**  
Observability, tracing, privacy

**Common Failure Modes**  
Logging entire prompts/responses unredacted; no correlation IDs.

**Production Considerations**  
Add distributed tracing backend and retention controls.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(obs): instrument end to end ai request traces`

**Portfolio Value**  
Shows production AI operations maturity.

---

### Day 96 — Research Day — Inference Optimization and Compression

**Role**  
Research Engineer / ML Engineer

**Business/Technical Scenario**  
A deployed model is accurate but too expensive at target latency.

**Problem Statement**  
Evaluate one or more optimization techniques under fixed quality constraints.

**Objective**  
Quantify quality–latency–memory trade-offs.

**Dataset / Data Source**  
Use Day 59/65 model or a small open-source model available locally; document exact model revision.

**Task**  
Compare baseline vs quantization/distillation/ONNX/TorchScript or batching; measure quality delta, latency, throughput, memory.

**Technologies**  
PyTorch + ONNX Runtime or bitsandbytes/quantization tooling + benchmark scripts

**Required Deliverables**  
research report; benchmark table; optimized artifact; decision memo.

**Acceptance Criteria**  
Benchmark workload fixed; metrics include p95 latency and quality; hardware documented; no fabricated speedups.

**Professional Skills Tested**  
Inference optimization, benchmarking, research

**Common Failure Modes**  
Reporting single-request latency; optimizing on synthetic inputs only.

**Production Considerations**  
Use representative production traces and rollback-ready artifacts.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`research: optimize ai inference under latency budget`

**Portfolio Value**  
Strong ML-systems research project.

---

### Day 97 — Enterprise AI Data Lifecycle and Governance

**Role**  
Data/AI Governance Engineer

**Business/Technical Scenario**  
The platform now processes customer data, documents, and model outputs.

**Problem Statement**  
Define lifecycle controls for data, embeddings, prompts, logs, and model artifacts.

**Objective**  
Make governance implementable, not only policy prose.

**Dataset / Data Source**  
Synthetic enterprise data and Day 90 platform; public docs only where rights allow.

**Task**  
Create data classification, retention, deletion, access-control matrix, lineage map, model/data version policy, and incident response checklist.

**Technologies**  
Python + PostgreSQL + GitHub + documentation tooling

**Required Deliverables**  
governance docs; lineage diagram; retention config; access matrix.

**Acceptance Criteria**  
Every sensitive artifact has owner, purpose, retention, and access policy; deletion implications are explicit.

**Professional Skills Tested**  
Governance, privacy, lifecycle management

**Common Failure Modes**  
Treating model outputs as unclassified; retaining everything forever.

**Production Considerations**  
Automate policy checks and deletion workflows where feasible.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`docs(governance): establish enterprise ai data lifecycle`

**Portfolio Value**  
Professional enterprise-readiness artifact.

---

### Day 98 — Production Debugging — RAG Latency Regression

**Role**  
AI/RAG Platform Engineer

**Business/Technical Scenario**  
RAG p95 latency exceeds the product SLO after adding reranking and multi-query retrieval.

**Problem Statement**  
Find the latency budget breach and rebalance the pipeline.

**Objective**  
Optimize without destroying retrieval quality.

**Dataset / Data Source**  
Day 90 service with synthetic trace logs and controlled traffic.

**Task**  
Break down latency by rewrite/retrieval/rerank/LLM stages; test candidate-k, reranker usage, caching, query routing, and parallelism; compare quality after fix.

**Technologies**  
Python + FastAPI + vector DB + benchmark tooling

**Required Deliverables**  
incident report; latency profile; patch; quality regression report.

**Acceptance Criteria**  
P95 meets the documented target or a justified target is updated; quality delta quantified; no hidden degradation.

**Professional Skills Tested**  
Performance engineering, RAG optimization, incident response

**Common Failure Modes**  
Making LLM smaller immediately; removing citations to gain speed.

**Production Considerations**  
Introduce adaptive retrieval depth and stage-level timeouts.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`perf(rag): restore rag latency within slo`

**Portfolio Value**  
Excellent production RAG troubleshooting evidence.

---

### Day 99 — Research Day — End-to-End AI System Benchmark

**Role**  
Research Engineer

**Business/Technical Scenario**  
The enterprise platform has multiple moving parts and leadership wants measurable proof of improvement.

**Problem Statement**  
Benchmark the whole system across data, ML, RAG, and deployment changes.

**Objective**  
Produce a defensible final technical evaluation.

**Dataset / Data Source**  
Day 90 platform plus fixed end-to-end evaluation set and representative synthetic load.

**Task**  
Baseline → improved retrieval/agent/ML component → ablation → throughput/latency → quality/security/error analysis → limitations → future work.

**Technologies**  
Python + MLflow + RAG eval + load testing + pandas

**Required Deliverables**  
final benchmark report; experiment artifacts; dashboard; architecture version comparison.

**Acceptance Criteria**  
All results trace to fixed configs/data/model versions; no fabricated claims; bottlenecks and limitations explicit.

**Professional Skills Tested**  
Systems research, benchmarking, scientific communication

**Common Failure Modes**  
Changing multiple variables without attribution; reporting only happy-path examples.

**Production Considerations**  
Publish a versioned benchmark suite to guard future releases.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`research: benchmark end to end enterprise ai platform`

**Portfolio Value**  
Capstone-level research evidence.

---

### Day 100 — Final Capstone — Enterprise AI Platform

**Role**  
Staff AI Engineer / MLOps Lead

**Business/Technical Scenario**  
The organization needs one production-shaped platform demonstrating the full professional stack.

**Problem Statement**  
Integrate data ingestion, processing, database, ML/AI, RAG, API, authentication, Docker, CI/CD, monitoring, evaluation, and documentation.

**Objective**  
Prove end-to-end engineering competence and production judgment.

**Dataset / Data Source**  
Combine verified public datasets where appropriate (DR02/DR04/DR08/DR09/DR11/DR12/DR13) plus clearly synthetic private-style operational data.

**Task**  
Build an enterprise platform with: ingestion→processing→DB→ML/AI→RAG→API→auth→Docker→CI/CD→monitoring→evaluation→documentation; provide architecture, operational runbook, security model, and demo.

**Technologies**  
Python + PostgreSQL + FastAPI + PyTorch/Transformers + RAG stack + MLflow + DVC + Docker + GitHub Actions

**Required Deliverables**  
complete repository; architecture; deployment files; tests; CI; model registry evidence; RAG eval; security tests; monitoring dashboard; runbooks; final report; demo.

**Acceptance Criteria**  
Clean clone setup works; critical tests green; model/RAG eval meets predeclared thresholds; auth/security tests pass; container health checks pass; monitoring emits usable signals; rollback procedure demonstrated.

**Professional Skills Tested**  
Systems architecture, Data Science, ML Engineering, AI Engineering, RAG, MLOps, DevOps, research, security

**Common Failure Modes**  
Scope explosion; undocumented glue code; no operational owner; unsupported claims about quality.

**Production Considerations**  
Treat production as lifecycle: backups, secrets, access control, observability, incident response, cost limits, model/data versioning, and controlled releases.

**Extension Challenge**  
Add one advanced enhancement that increases reliability, scale, or evaluation rigor.

**Git Commit**  
`feat(capstone): ship enterprise ai platform`

**Portfolio Value**  
Final portfolio centerpiece covering Data Analyst → Data Scientist → ML Engineer → AI Engineer → MLOps → RAG → Research Engineer.

---


