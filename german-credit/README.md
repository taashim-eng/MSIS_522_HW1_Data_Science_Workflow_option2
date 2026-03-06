# Statlog (German Credit Data)

## Provenance
- **Source**: UCI Machine Learning Repository
- **URL**: https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data)
- **Donated by**: Professor Dr. Hans Hofmann, University of Hamburg (1994)
- **License**: CC BY 4.0

## Description
Classifies 1,000 individuals as good (1) or bad (2) credit risks using 20 attributes covering financial history, personal demographics, and loan details.

## Files
| File | Description | Size |
|------|-------------|------|
| `german.data` | Main dataset, space-separated, 21 columns (no header) | 79,793 B |
| `german.data-numeric` | Numeric-only version (binary-coded categoricals) | 102,000 B |
| `german.doc` | Documentation / data dictionary | 4,679 B |

## Preprocessing Steps
1. Load with `pd.read_csv('german.data', sep=' ', header=None, names=[...])` — see column names in `german.doc`
2. Remap target: `Class` → 1=Good → 0 (no default), 2=Bad → 1 (default)
3. Encode categoricals: one-hot or ordinal encode `Status_checking_acct`, `Credit_history`, `Purpose`, `Savings_acct`, `Personal_status_sex`, etc.
4. No missing values — skip imputation

## Target Variable
`Class` (column 21): 1 = Good credit, 2 = Bad credit  
Remap to: 0 = Good (no default), 1 = Bad (default)

## Sample Command
```python
import pandas as pd
cols = ['Status_checking_acct','Duration','Credit_history','Purpose','Credit_amount',
        'Savings_acct','Present_employment','Installment_rate','Personal_status_sex',
        'Other_debtors','Residence_since','Property','Age','Other_installment_plans',
        'Housing','Existing_credits','Job','Num_dependents','Telephone','Foreign_worker','Class']
df = pd.read_csv('german.data', sep=' ', header=None, names=cols)
df['Class'] = df['Class'].map({1: 0, 2: 1})
sample = df.sample(n=200, random_state=42)
sample.to_csv('../sample.csv', index=False)
```
