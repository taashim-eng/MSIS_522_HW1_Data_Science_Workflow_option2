# Alternative Credit Scoring — Dataset Research & HW1 Alignment

**Course:** MSIS 522 B — Advanced Machine Learning  
**Assignment:** Homework 1 — The Complete Data Science Workflow  
**Date:** 2026-03-05  
**Author:** Taashi M.

---

## 1. Executive Summary

This report identifies, evaluates, and documents **six candidate tabular datasets** suitable for building explainable alternative credit-scoring models. The datasets span classical credit-risk benchmarks (German Credit, Taiwan Default, FICO HELOC), Kaggle competition data (Give Me Some Credit, Home Credit Default Risk), and peer-to-peer lending records (LendingClub). Each dataset supports **binary classification** tasks aligned with MSIS 522 HW1: predicting whether a borrower will default.

**Top 2 recommendations for HW1:**

| Rank | Dataset | Why |
|------|---------|-----|
| **#1** | Taiwan Default of Credit Card Clients | 30K rows, single CSV, clean binary target, demographic features for fairness analysis, well-documented in academic literature |
| **#2** | Statlog German Credit | 1K-row classic benchmark, interpretable features, built-in fairness concerns (personal status/sex, foreign worker), fast prototyping |

Both are **directly downloadable without credentials** and satisfy all HW1 requirements: ≥200 rows, clear target variable, tabular format, and real-world provenance.

---

## 2. Dataset Inventory

### Dataset 1: Statlog (German Credit Data)

| Attribute | Detail |
|-----------|--------|
| **Title** | Statlog (German Credit Data) |
| **Summary** | Classify 1,000 bank customers as good or bad credit risks using 20 financial/demographic features. |
| **Source** | UCI Machine Learning Repository |
| **Direct URL** | `https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data` |
| **Download cmd** | `curl -O https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data` |
| **Files** | `german.data` (79,793 B), `german.data-numeric` (102,000 B), `german.doc` (4,679 B) |
| **Format** | Space-separated text, no header |
| **Shape** | 1,000 rows × 21 columns |
| **Target** | `Class` — 1 = Good, 2 = Bad |
| **Key fields** | `Status_checking_acct`, `Duration`, `Credit_history`, `Purpose`, `Credit_amount`, `Savings_acct`, `Age`, `Personal_status_sex`, `Foreign_worker` |
| **License** | CC BY 4.0 |
| **Missing values** | 0 |
| **PII risk** | None — fully anonymized categorical codes |

**Sample extraction:**
```python
import pandas as pd
cols = ['Status_checking_acct','Duration','Credit_history','Purpose','Credit_amount',
        'Savings_acct','Present_employment','Installment_rate','Personal_status_sex',
        'Other_debtors','Residence_since','Property','Age','Other_installment_plans',
        'Housing','Existing_credits','Job','Num_dependents','Telephone','Foreign_worker','Class']
df = pd.read_csv('german-credit/raw/german.data', sep=' ', header=None, names=cols)
sample = df.sample(n=200, random_state=42)
sample.to_csv('german-credit/sample.csv', index=False)
```

**HW1 Mapping:** This dataset supports all five models (Logistic Regression baseline, Decision Tree, Random Forest, XGBoost, MLP) with its mix of categorical and numeric features. The `Personal_status_sex` and `Foreign_worker` columns make it ideal for Tab 5 Ethics & Bias analysis (disparate impact by gender, nationality). Its small size allows rapid GridSearchCV iteration. SHAP waterfall plots are straightforward since the feature space is interpretable. For Tab 4, expose sliders for `Duration`, `Credit_amount`, `Age`, and dropdowns for `Purpose`, `Status_checking_acct`.

#### 10-Row Preview

| Status_checking_acct | Duration | Credit_history | Purpose | Credit_amount | Savings_acct | Age | Class |
|-----|------|------|------|------|------|-----|------|
| A11 | 6 | A34 | A43 | 1169 | A65 | 67 | 1 |
| A12 | 48 | A32 | A43 | 5951 | A61 | 22 | 2 |
| A14 | 12 | A34 | A46 | 2096 | A61 | 49 | 1 |
| A11 | 42 | A32 | A42 | 7882 | A61 | 45 | 1 |
| A11 | 24 | A33 | A40 | 4870 | A61 | 53 | 2 |
| A14 | 36 | A32 | A46 | 9055 | A65 | 35 | 1 |
| A14 | 24 | A32 | A42 | 2835 | A63 | 53 | 1 |
| A12 | 36 | A32 | A41 | 6948 | A61 | 35 | 1 |
| A14 | 12 | A32 | A43 | 3059 | A64 | 61 | 1 |
| A12 | 30 | A34 | A40 | 5234 | A61 | 28 | 2 |

---

### Dataset 2: Default of Credit Card Clients (Taiwan)

| Attribute | Detail |
|-----------|--------|
| **Title** | Default of Credit Card Clients |
| **Summary** | Predict whether 30,000 Taiwan credit-card holders will default on payment next month. |
| **Source** | UCI Machine Learning Repository |
| **Direct URL** | `https://archive.ics.uci.edu/static/public/350/default+of+credit+card+clients.zip` |
| **Download cmd** | `curl -LO https://archive.ics.uci.edu/static/public/350/default+of+credit+card+clients.zip && unzip default+of+credit+card+clients.zip` |
| **Files** | `default of credit card clients.xls` (5,539,328 B) |
| **Format** | Excel (.xls), header on row 2 |
| **Shape** | 30,000 rows × 25 columns (incl. ID) |
| **Target** | `default payment next month` — 0 = No, 1 = Yes |
| **Key fields** | `LIMIT_BAL`, `SEX`, `EDUCATION`, `MARRIAGE`, `AGE`, `PAY_0`–`PAY_6` (repayment status), `BILL_AMT1`–`BILL_AMT6`, `PAY_AMT1`–`PAY_AMT6` |
| **License** | CC BY 4.0 |
| **Missing values** | 0 |
| **PII risk** | None — anonymized IDs, no names/addresses |

**Sample extraction:**
```python
import pandas as pd
df = pd.read_excel('taiwan-credit/raw/default of credit card clients.xls', header=1)
sample = df.sample(n=200, random_state=42)
sample.to_csv('taiwan-credit/sample.csv', index=False)
```

**HW1 Mapping:** The **recommended primary dataset for HW1**. At 30K rows, it provides robust training for all five models. The 6-month payment history (`PAY_0`–`PAY_6`) and billing amounts offer rich numeric features for SHAP interpretation. `SEX`, `EDUCATION`, `MARRIAGE`, and `AGE` enable fairness auditing (Tab 5). For Tab 4 interactive predictions, expose sliders for `LIMIT_BAL`, `AGE`, and `PAY_0` (most recent payment status), with dropdowns for `SEX`, `EDUCATION`, `MARRIAGE`; use mean/mode for remaining features. Class imbalance (~22% default) requires handling via SMOTE or `class_weight='balanced'`.

#### 10-Row Preview

| ID | LIMIT_BAL | SEX | EDUCATION | MARRIAGE | AGE | PAY_0 | PAY_2 | PAY_3 | PAY_4 | PAY_5 | PAY_6 | BILL_AMT1 | default payment next month |
|-----|-----------|-----|-----------|----------|-----|-------|-------|-------|-------|-------|-------|-----------|---------------------------|
| 1 | 20000 | 2 | 2 | 1 | 24 | 2 | 2 | -1 | -1 | -2 | -2 | 3913 | 1 |
| 2 | 120000 | 2 | 2 | 2 | 26 | -1 | 2 | 0 | 0 | 0 | 2 | 2682 | 1 |
| 3 | 90000 | 2 | 2 | 2 | 34 | 0 | 0 | 0 | 0 | 0 | 0 | 29239 | 0 |
| 4 | 50000 | 2 | 2 | 1 | 37 | 0 | 0 | 0 | 0 | 0 | 0 | 46990 | 0 |
| 5 | 50000 | 1 | 2 | 1 | 57 | -1 | 0 | -1 | 0 | 0 | 0 | 8617 | 0 |
| 6 | 500000 | 1 | 1 | 2 | 37 | 0 | 0 | 0 | 0 | 0 | 0 | 64400 | 0 |
| 7 | 100000 | 1 | 2 | 2 | 29 | 0 | 0 | 0 | 0 | 0 | 0 | 367965 | 0 |
| 8 | 100000 | 2 | 2 | 2 | 23 | 0 | -1 | -1 | 0 | 0 | -1 | 11876 | 0 |
| 9 | 80000 | 2 | 2 | 1 | 28 | 0 | 0 | 2 | 0 | 0 | 0 | 11285 | 0 |
| 10 | 300000 | 1 | 1 | 2 | 35 | -2 | -2 | -2 | -2 | -1 | -1 | 0 | 0 |

---

### Dataset 3: FICO HELOC (Home Equity Line of Credit)

| Attribute | Detail |
|-----------|--------|
| **Title** | FICO Explainable ML Challenge — HELOC Dataset |
| **Summary** | Predict "good/bad" repayment performance on 10,459 home equity line-of-credit applications using 23 credit-bureau features. |
| **Source** | FICO Community / GitHub mirror |
| **Direct URL** | `https://raw.githubusercontent.com/benoitparis/explainable-challenge/master/heloc_dataset_v1.csv` |
| **Download cmd** | `curl -O https://raw.githubusercontent.com/benoitparis/explainable-challenge/master/heloc_dataset_v1.csv` |
| **Files** | `heloc_dataset_v1.csv` (678,479 B) |
| **Format** | CSV with header |
| **Shape** | 10,459 rows × 24 columns |
| **Target** | `RiskPerformance` — "Good" or "Bad" |
| **Key fields** | `ExternalRiskEstimate`, `MSinceOldestTradeOpen`, `NumSatisfactoryTrades`, `PercentTradesNeverDelq`, `NetFractionRevolvingBurden`, `NumInqLast6M` |
| **License** | Research use (FICO Explainable ML Challenge terms) |
| **Missing values** | 0 (but sentinel value `-7` = "Condition not Met", `-8` = "No Usable/Valid Trades", `-9` = "No Bureau Record") |
| **PII risk** | None — all credit-bureau aggregates |

**Sample extraction:**
```python
import pandas as pd
df = pd.read_csv('fico-heloc/raw/heloc_dataset_v1.csv')
sample = df.sample(n=200, random_state=42)
sample.to_csv('fico-heloc/sample.csv', index=False)
```

**HW1 Mapping:** This dataset was designed specifically for **explainable machine learning**. All 23 features are numeric credit-bureau aggregates, making SHAP analysis especially clear. The sentinel values (-7, -8, -9) require pre-processing (replace with NaN or encode). No demographic features, so fairness analysis must focus on algorithmic bias rather than protected attributes. For Tab 4, expose sliders for `ExternalRiskEstimate`, `NumSatisfactoryTrades`, `PercentTradesNeverDelq`, `NetFractionRevolvingBurden`; average remaining features.

#### 10-Row Preview

| RiskPerformance | ExternalRiskEstimate | MSinceOldestTradeOpen | AverageMInFile | NumSatisfactoryTrades | PercentTradesNeverDelq | NumTotalTrades |
|-----------------|---------------------|-----------------------|----------------|-----------------------|------------------------|----------------|
| Bad | 55 | 144 | 84 | 20 | 83 | 23 |
| Bad | 61 | 58 | 41 | 2 | 100 | 7 |
| Bad | 67 | 66 | 24 | 9 | 100 | 9 |
| Bad | 66 | 169 | 73 | 28 | 93 | 30 |
| Bad | 81 | 333 | 132 | 12 | 100 | 12 |
| Bad | 59 | 137 | 78 | 31 | 91 | 32 |
| Good | 54 | 88 | 37 | 25 | 92 | 26 |
| Good | 68 | 148 | 65 | 17 | 83 | 18 |
| Bad | 59 | 324 | 138 | 24 | 85 | 27 |
| Bad | 61 | 79 | 36 | 19 | 95 | 19 |

---

### Dataset 4: Give Me Some Credit (Kaggle)

| Attribute | Detail |
|-----------|--------|
| **Title** | Give Me Some Credit |
| **Summary** | Predict financial distress within 2 years for 150,000 borrowers using 10 financial features. |
| **Source** | Kaggle Competition |
| **Kaggle slug** | `competitions/GiveMeSomeCredit` |
| **Download cmd** | `kaggle competitions download -c GiveMeSomeCredit -p give-me-some-credit/raw/` |
| **Credentials** | Set `KAGGLE_USERNAME` and `KAGGLE_KEY` environment variables (`$env:KAGGLE_USERNAME = "your_username"`) |
| **Files** | `cs-training.csv` (~10 MB), `cs-test.csv` (~5 MB), `Data Dictionary.xls`, `sampleEntry.csv` |
| **Format** | CSV with header |
| **Shape** | ~150,000 rows × 11 columns |
| **Target** | `SeriousDlqin2yrs` — 0 = No, 1 = Yes |
| **Key fields** | `RevolvingUtilizationOfUnsecuredLines`, `age`, `NumberOfTime30-59DaysPastDueNotWorse`, `DebtRatio`, `MonthlyIncome`, `NumberOfOpenCreditLinesAndLoans`, `NumberRealEstateLoansOrLines`, `NumberOfDependents` |
| **License** | Kaggle Competition Rules |
| **Missing values** | ~29,000 in `MonthlyIncome`, ~3,900 in `NumberOfDependents` |
| **PII risk** | None — anonymized |

**Sample extraction:**
```python
import pandas as pd
df = pd.read_csv('give-me-some-credit/raw/cs-training.csv', index_col=0)
sample = df.sample(n=200, random_state=42)
sample.to_csv('give-me-some-credit/sample.csv', index=False)
```

**HW1 Mapping:** Large training set for robust model comparison. Missing values in `MonthlyIncome` and `NumberOfDependents` demonstrate imputation techniques. The `age` field supports basic fairness checks. Target is imbalanced (~6.7% positive), motivating SMOTE or class weighting. Good candidate for demonstrating the full GridSearchCV pipeline due to ample data.

---

### Dataset 5: Home Credit Default Risk (Kaggle)

| Attribute | Detail |
|-----------|--------|
| **Title** | Home Credit Default Risk |
| **Summary** | Predict loan repayment ability for 307K+ applicants using multi-table financial data (applications, bureau records, past loans). |
| **Source** | Kaggle Competition |
| **Kaggle slug** | `competitions/home-credit-default-risk` |
| **Download cmd** | `kaggle competitions download -c home-credit-default-risk -p home-credit-default-risk/raw/` |
| **Credentials** | Set `KAGGLE_USERNAME` and `KAGGLE_KEY` environment variables |
| **Files** | `application_train.csv` (~307K rows), `application_test.csv`, `bureau.csv`, `bureau_balance.csv`, `POS_CASH_balance.csv`, `credit_card_balance.csv`, `previous_application.csv`, `installments_payments.csv` |
| **Format** | CSV with header |
| **Shape** | 307,511 rows × 122 columns (main table) |
| **Target** | `TARGET` — 0 = Repaid, 1 = Default |
| **Key fields** | `AMT_INCOME_TOTAL`, `AMT_CREDIT`, `AMT_ANNUITY`, `NAME_CONTRACT_TYPE`, `CODE_GENDER`, `DAYS_BIRTH`, `DAYS_EMPLOYED`, `EXT_SOURCE_1/2/3` |
| **License** | Kaggle Competition Rules |
| **Missing values** | Significant across many columns (60+ columns have >50% missing) |
| **PII risk** | None — anonymized with encoded categories |

**Sample extraction:**
```python
import pandas as pd
df = pd.read_csv('home-credit-default-risk/raw/application_train.csv')
sample = df.sample(n=200, random_state=42)
sample.to_csv('home-credit-default-risk/sample.csv', index=False)
```

**HW1 Mapping:** The richest dataset with relational tables supporting advanced feature engineering. However, its 122 columns and multi-table structure may be **overly complex for HW1** — better suited for a semester project. The `CODE_GENDER` field enables fairness analysis. Has severe class imbalance (~8% default).

---

### Dataset 6: LendingClub Loan Data (Kaggle)

| Attribute | Detail |
|-----------|--------|
| **Title** | Lending Club Loans 2007-2020 |
| **Summary** | Peer-to-peer lending records for ~2.9M loans with 151 features covering borrower profiles, loan details, and outcomes. |
| **Source** | Kaggle |
| **Kaggle slug** | `datasets/ethon0426/lending-club-20072020q1` |
| **Download cmd** | `kaggle datasets download -d ethon0426/lending-club-20072020q1 -p lendingclub-loans/raw/` |
| **Credentials** | Set `KAGGLE_USERNAME` and `KAGGLE_KEY` environment variables |
| **Files** | `accepted_2007_to_2018Q4.csv.gz` (~640 MB uncompressed) |
| **Format** | Compressed CSV |
| **Shape** | ~2,900,000 rows × 151 columns |
| **Target** | `loan_status` — map "Charged Off" = 1, "Fully Paid" = 0 |
| **Key fields** | `loan_amnt`, `int_rate`, `annual_inc`, `dti`, `delinq_2yrs`, `fico_range_low`, `open_acc`, `pub_rec`, `purpose`, `addr_state`, `emp_length` |
| **License** | CC0 Public Domain |
| **Missing values** | Substantial across many columns |
| **PII risk** | Low — `addr_state` and `zip_code` (3-digit) may be quasi-identifiers; redact or generalize for privacy |

**Sample extraction:**
```python
import pandas as pd
df = pd.read_csv('lendingclub-loans/raw/accepted_2007_to_2018Q4.csv.gz', nrows=50000)
# Filter to completed loans only
df = df[df['loan_status'].isin(['Fully Paid', 'Charged Off'])]
sample = df.sample(n=200, random_state=42)
sample.to_csv('lendingclub-loans/sample.csv', index=False)
```

**HW1 Mapping:** Real-world P2P lending data with rich features. However, the 2.9M-row size requires subsampling, and 151 columns need significant feature selection. Best for students wanting to demonstrate scalable pipelines. `addr_state` enables geographic fairness analysis.

---

## 3. Top 2 Recommendation & Justification

### 🥇 Primary Recommendation: Taiwan Default of Credit Card Clients

**Why:**
1. **Right size**: 30,000 rows — large enough for meaningful train/test splits and GridSearchCV, small enough for fast MLP training
2. **Clean**: Zero missing values, single file, straightforward Excel import
3. **Binary classification**: Clear target (`default payment next month`)
4. **Fairness-ready**: `SEX` (gender), `EDUCATION`, `MARRIAGE`, `AGE` enable Tab 5 disparate-impact and equalized-odds analysis
5. **SHAP-friendly**: Mix of categorical (encoded as integers) and continuous features produces interpretable SHAP plots
6. **Class imbalance**: ~22% default rate — enough to motivate SMOTE/class-weighting, not so extreme as to collapse metrics
7. **Academic pedigree**: Published in Yeh & Lien (2009), widely used in ML coursework

### 🥈 Secondary Recommendation: Statlog German Credit

**Why:**
1. **Fast prototyping**: 1,000 rows — entire pipeline runs in seconds
2. **Interpretable**: 20 features with clear business meaning
3. **Ethics showcase**: `Personal_status_sex`, `Foreign_worker`, `Age` are textbook fairness-audit examples
4. **Proven benchmark**: One of the most-cited credit datasets in ML literature
5. **Complementary**: If used alongside Taiwan Credit, demonstrates model behavior on small vs. medium datasets

---

## 4. EDA Plan (Top 2 Picks)

### Taiwan Default of Credit Card Clients

| EDA Step | Detail |
|----------|--------|
| **Distributions** | Histograms for `LIMIT_BAL`, `AGE`, `BILL_AMT1`–`BILL_AMT6` |
| **Target balance** | Bar chart of `default payment next month` (0 vs. 1) |
| **Correlation** | Heatmap of all numeric features (expect high correlation among `BILL_AMT` and `PAY_AMT` series) |
| **Cross-tabs** | Default rate by `SEX`, `EDUCATION`, `MARRIAGE` |
| **Outlier detection** | Box plots for `LIMIT_BAL`, `BILL_AMT1`, `PAY_AMT1` |
| **Payment patterns** | Stacked bar chart of `PAY_0`–`PAY_6` distributions |

### Statlog German Credit

| EDA Step | Detail |
|----------|--------|
| **Distributions** | Histograms for `Duration`, `Credit_amount`, `Age` |
| **Target balance** | Bar chart of `Class` (1=Good vs. 2=Bad; note: 70/30 split) |
| **Cross-tabs** | Default rate by `Personal_status_sex`, `Foreign_worker`, `Purpose` |
| **Correlation** | Heatmap of numeric features (after encoding categoricals) |
| **Feature importance** | Preliminary Random Forest importance plot |

---

## 5. Feature Engineering Suggestions

### Taiwan Credit
- **Payment behavior aggregates**: `avg_delay = mean(PAY_0..PAY_6)`, `max_delay`, `num_months_delayed`
- **Utilization ratio**: `BILL_AMT1 / LIMIT_BAL`
- **Payment ratio**: `PAY_AMT1 / BILL_AMT1` (how much of the bill was paid)
- **Trend features**: Slope of `BILL_AMT1..BILL_AMT6` over time (increasing debt trend)
- **Age bins**: Discretize `AGE` into brackets for fairness subgroup analysis

### German Credit
- **Encode categoricals**: One-hot or ordinal encoding for `Status_checking_acct`, `Credit_history`, `Purpose`, etc.
- **Interaction features**: `Credit_amount × Duration`, `Age × Present_employment`
- **Binary flags**: `has_telephone`, `is_foreign_worker`
- **Risk score proxy**: Combine `Status_checking_acct` + `Savings_acct` into liquidity score

---

## 6. Baseline Model Plan

### Train/Test Split
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
```

### Model Pipeline

| # | Model | Implementation | Hyperparameter Tuning |
|---|-------|----------------|-----------------------|
| 1 | **Logistic Regression** | `sklearn.linear_model.LogisticRegression` | Baseline — default params |
| 2 | **Decision Tree** | `sklearn.tree.DecisionTreeClassifier` | GridSearchCV(5-fold): `max_depth=[3,5,7,10]`, `min_samples_leaf=[5,10,20,50]` |
| 3 | **Random Forest** | `sklearn.ensemble.RandomForestClassifier` | GridSearchCV(5-fold): `n_estimators=[50,100,200]`, `max_depth=[3,5,8]` |
| 4 | **XGBoost** | `xgboost.XGBClassifier` | GridSearchCV(5-fold): `learning_rate=[0.01,0.1,0.3]`, `n_estimators=[50,100,200]`, `max_depth=[3,5,7]` |
| 5 | **MLP** | `keras.Sequential` | ≥2 hidden layers (128 units, ReLU), output sigmoid, binary crossentropy |

### Evaluation Metrics
- **Accuracy**, **Precision**, **Recall**, **F1-Score**, **ROC-AUC**
- Confusion matrix for each model
- ROC curve comparison plot

---

## 7. Fairness & Audit Checklist

### Disparate Impact Analysis
```python
# For Taiwan Credit — check default predictions by SEX
from sklearn.metrics import confusion_matrix
male_preds = model.predict(X_test[X_test['SEX'] == 1])
female_preds = model.predict(X_test[X_test['SEX'] == 2])
# Disparate impact ratio = P(favorable|unprivileged) / P(favorable|privileged)
```

### Checklist
- [ ] **Data bias**: Check class distribution across protected attributes (`SEX`, `AGE`, `EDUCATION`, `MARRIAGE`)
- [ ] **Disparate impact**: Compute DI ratio for each model; flag if < 0.8 (four-fifths rule)
- [ ] **Equalized odds**: Compare TPR and FPR across subgroups
- [ ] **Calibration**: Check if predicted probabilities are well-calibrated per subgroup
- [ ] **Feature influence**: Use SHAP to check if protected attributes have outsized importance
- [ ] **Mitigation**: If bias detected, consider: removing protected features, reweighting, or post-processing threshold adjustment
- [ ] **Documentation**: Record all findings in Tab 5 of Streamlit app

---

## 8. Streamlit App Wireframe

### Tab 1: Executive Summary
- Problem statement and dataset description
- Key findings in bullet points
- Best model name and its AUC-ROC score

### Tab 2: Descriptive Analytics
- `st.dataframe(df.head())` — interactive data preview
- `st.write(df.describe())` — summary statistics
- Plotly/Matplotlib histograms for key features
- Seaborn correlation heatmap

### Tab 3: Model Performance
- Comparison table: all 5 models × 5 metrics
- Bar chart: AUC-ROC comparison
- ROC curves overlay (one per model)
- Best model's confusion matrix

### Tab 4: Predictions & Explainability
- **Interactive inputs:**
  - `st.slider("Credit Limit", 10000, 800000, 150000)` — `LIMIT_BAL`
  - `st.slider("Age", 20, 80, 35)` — `AGE`
  - `st.selectbox("Sex", [1, 2])` — `SEX` (1=Male, 2=Female)
  - `st.selectbox("Education", [1, 2, 3, 4])` — `EDUCATION`
  - `st.selectbox("Marriage", [1, 2, 3])` — `MARRIAGE`
  - `st.slider("Most Recent Payment Status", -2, 8, 0)` — `PAY_0`
  - Remaining features (`BILL_AMT`, `PAY_AMT`) use **averaged defaults** from training data
- **Output:** Prediction probability + SHAP waterfall plot for the input

### Tab 5: Ethics & Responsible AI
- Bias analysis results (disparate impact table)
- Equalized odds comparison chart
- Discussion of societal impact
- Mitigation strategies applied/recommended

---

## 9. CV Strategy

```python
from sklearn.model_selection import GridSearchCV, StratifiedKFold

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Example: Random Forest
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 8]
}
grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42, class_weight='balanced'),
    param_grid, cv=cv, scoring='roc_auc', n_jobs=-1
)
grid_search.fit(X_train, y_train)
```

---

## 10. Appendix: Kaggle CLI Setup

### Step 1: Install Kaggle CLI
```bash
pip install kaggle
```

### Step 2: Set Credentials
```powershell
$env:KAGGLE_USERNAME = "your_kaggle_username"
$env:KAGGLE_KEY = "your_kaggle_api_key"
```
Or create `%USERPROFILE%\.kaggle\kaggle.json`:
```json
{"username": "your_kaggle_username", "key": "your_kaggle_api_key"}
```

### Step 3: Download Datasets
```bash
# Give Me Some Credit
kaggle competitions download -c GiveMeSomeCredit -p give-me-some-credit/raw/

# Home Credit Default Risk
kaggle competitions download -c home-credit-default-risk -p home-credit-default-risk/raw/

# LendingClub Loans
kaggle datasets download -d ethon0426/lending-club-20072020q1 -p lendingclub-loans/raw/
```

### Step 4: To obtain your API key
1. Go to https://www.kaggle.com/settings
2. Scroll to "API" section
3. Click "Create New Token"
4. Download `kaggle.json` and place it in `%USERPROFILE%\.kaggle\`
