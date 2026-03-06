# MSIS 522 HW1 — Alternative Credit Scoring (Option 2)

## 📋 Project Overview

Research, download, and document high-quality tabular datasets for building **explainable alternative credit-scoring models** as part of MSIS 522 Advanced Machine Learning, Homework 1: The Complete Data Science Workflow.

## 🏆 Recommended Datasets

| Rank | Dataset | Rows | Cols | Target | Source |
|------|---------|------|------|--------|--------|
| **#1** | [Taiwan Default of Credit Card Clients](taiwan-credit/) | 30,000 | 25 | `default payment next month` | UCI |
| **#2** | [Statlog German Credit](german-credit/) | 1,000 | 21 | `Class` (1=Good, 2=Bad) | UCI |

### Additional Candidates
| Dataset | Rows | Cols | Source |
|---------|------|------|--------|
| [FICO HELOC](fico-heloc/) | 10,459 | 24 | FICO / GitHub |
| [Give Me Some Credit](give-me-some-credit/) | 150,000 | 11 | Kaggle |
| [Home Credit Default Risk](home-credit-default-risk/) | 307,511 | 122 | Kaggle |
| [LendingClub Loans](lendingclub-loans/) | 2,900,000 | 151 | Kaggle |

## 📁 Repository Structure

```
├── research_writeup.md          # Full research report
├── research_writeup.html        # Styled HTML (print to PDF)
├── datasets_manifest.json       # File inventory with SHA-256 checksums
├── commands.sh                  # Download commands
├── run_log.txt                  # Execution log
├── german-credit/               # Dataset 1 (downloaded)
│   ├── README.md
│   ├── sample.csv               # 200-row sample
│   └── raw/                     # Full dataset files
├── taiwan-credit/               # Dataset 2 (downloaded)
│   ├── README.md
│   ├── sample.csv
│   └── raw/                     # Full dataset files
├── fico-heloc/                  # Dataset 3 (downloaded)
│   ├── README.md
│   ├── sample.csv
│   └── raw/
├── give-me-some-credit/         # Dataset 4 (Kaggle CLI)
│   └── README.md
├── home-credit-default-risk/    # Dataset 5 (Kaggle CLI)
│   └── README.md
└── lendingclub-loans/           # Dataset 6 (Kaggle CLI)
    └── README.md
```

## 🚀 Quick Start

### 1. Directly Available Datasets (already downloaded)
German Credit, Taiwan Credit, and FICO HELOC raw files are in their respective `raw/` folders. 200-row samples are in each dataset's `sample.csv`.

### 2. Kaggle Datasets (require credentials)
```powershell
# Set credentials
$env:KAGGLE_USERNAME = "your_username"
$env:KAGGLE_KEY = "your_api_key"

# Download any of:
kaggle competitions download -c GiveMeSomeCredit -p give-me-some-credit/raw/
kaggle competitions download -c home-credit-default-risk -p home-credit-default-risk/raw/
kaggle datasets download -d ethon0426/lending-club-20072020q1 -p lendingclub-loans/raw/
```

## 🔬 HW1 Model Pipeline

| # | Model | Tuning |
|---|-------|--------|
| 1 | Logistic Regression | Baseline |
| 2 | Decision Tree | GridSearchCV: `max_depth`, `min_samples_leaf` |
| 3 | Random Forest | GridSearchCV: `n_estimators`, `max_depth` |
| 4 | XGBoost | GridSearchCV: `learning_rate`, `n_estimators`, `max_depth` |
| 5 | MLP (Keras) | ≥2 hidden layers, ReLU |

**Split:** 70/30, `random_state=42` | **CV:** StratifiedKFold(5)

## 📊 Evaluation
Accuracy, Precision, Recall, F1-Score, ROC-AUC

## ⚖️ Fairness
Disparate impact, equalized odds across `SEX`, `AGE`, `EDUCATION`, `MARRIAGE`

---
*MSIS 522 B — Advanced Machine Learning | University of Washington*
