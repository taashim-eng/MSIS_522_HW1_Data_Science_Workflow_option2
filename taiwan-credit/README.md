# Default of Credit Card Clients (Taiwan)

## Provenance
- **Source**: UCI Machine Learning Repository
- **URL**: https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients
- **Published by**: I-Cheng Yeh, Che-hui Lien (2009)
- **Paper**: "The comparisons of data mining techniques for the predictive accuracy of probability of default of credit card clients" — Expert Systems with Applications, 36(2), 2473-2480
- **License**: CC BY 4.0

## Description
Predicts whether 30,000 Taiwan credit card holders will default on their payment next month, using 23 features including demographics, credit limit, payment history (6 months), and bill/payment amounts.

## Files
| File | Description | Size |
|------|-------------|------|
| `default of credit card clients.xls` | Main dataset, Excel format, header on row 2 | 5,539,328 B |
| `default_credit_card_clients.zip` | Original ZIP archive | 5,539,494 B |

## Preprocessing Steps
1. Load with `pd.read_excel('default of credit card clients.xls', header=1)`
2. Drop `ID` column (not a feature)
3. Rename target: `default payment next month` → `default` for convenience
4. Verify encoding: `SEX` (1=Male, 2=Female), `EDUCATION` (1=Graduate, 2=University, 3=High school, 4=Others), `MARRIAGE` (1=Married, 2=Single, 3=Others)
5. Handle `PAY_0`–`PAY_6` values: -2=No consumption, -1=Pay duly, 0=Revolving credit, 1–9=Months delayed
6. No missing values
7. For fairness analysis: create binary protected attributes (e.g., `is_female = (SEX == 2)`)

## Target Variable
`default payment next month`: 0 = No default, 1 = Default

## Class Distribution
- 0 (No default): ~23,364 (77.9%)
- 1 (Default): ~6,636 (22.1%)

## Sample Command
```python
import pandas as pd
df = pd.read_excel('default of credit card clients.xls', header=1)
df = df.drop(columns=['ID'])
sample = df.sample(n=200, random_state=42)
sample.to_csv('../sample.csv', index=False)
```
