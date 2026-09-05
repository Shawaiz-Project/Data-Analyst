



# 100 Days of Professional Data Scientist + AI/ML Engineer
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

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

| ID | Dataset | Source URL | Approx.|
|-|-|-|-|mat | Task | Target | Major challenges |
|-|-|-|-|-|-|-||------------|----------------------|------|--------|------------------|
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
