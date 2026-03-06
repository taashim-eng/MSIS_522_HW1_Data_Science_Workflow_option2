# FICO HELOC (Home Equity Line of Credit)

## Provenance
- **Source**: FICO Explainable Machine Learning Challenge
- **URL**: https://community.fico.com/s/explainable-machine-learning-challenge
- **Mirror**: https://github.com/benoitparis/explainable-challenge
- **License**: Research use (FICO Explainable ML Challenge terms)

## Description
10,459 home equity line of credit (HELOC) applications with 23 credit-bureau aggregate features. Designed specifically for explainable ML research. Target indicates whether the applicant made timely payments ("Good") or was 90+ days delinquent ("Bad").

## Files
| File | Description | Size |
|------|-------------|------|
| `heloc_dataset_v1.csv` | Main dataset, CSV with header, 24 columns | 678,479 B |

## Preprocessing Steps
1. Load with `pd.read_csv('heloc_dataset_v1.csv')`
2. Encode target: `RiskPerformance` → "Good" = 0, "Bad" = 1
3. Handle sentinel values:
   - `-7` = "Condition not Met" → consider as NaN or separate category
   - `-8` = "No Usable/Valid Trades or Inquiries" → consider as NaN
   - `-9` = "No Bureau Record or Public Record" → consider as NaN
4. After replacing sentinels with NaN, impute with median or create binary indicator columns
5. All features are numeric — no categorical encoding needed

## Target Variable
`RiskPerformance`: "Good" (timely) or "Bad" (90+ days delinquent)

## Key Features
- `ExternalRiskEstimate` — Consolidated external risk score
- `MSinceOldestTradeOpen` — Months since oldest trade opened
- `NumSatisfactoryTrades` — Number of satisfactory trades
- `PercentTradesNeverDelq` — Percent of trades never delinquent
- `NetFractionRevolvingBurden` — Net revolving credit utilization
- `NumInqLast6M` — Number of inquiries in last 6 months

## Notes
- No demographic features (no gender, age, ethnicity) — fairness analysis must focus on algorithmic fairness (e.g., prediction calibration across risk score ranges) rather than protected-attribute analysis
- Sentinel values (-7, -8, -9) are meaningful — document your handling approach

## Sample Command
```python
import pandas as pd
df = pd.read_csv('heloc_dataset_v1.csv')
df['RiskPerformance'] = df['RiskPerformance'].map({'Good': 0, 'Bad': 1})
sample = df.sample(n=200, random_state=42)
sample.to_csv('../sample.csv', index=False)
```
