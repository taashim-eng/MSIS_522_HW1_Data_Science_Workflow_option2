# Home Credit Default Risk (Kaggle)

## Provenance
- **Source**: Kaggle Competition
- **URL**: https://www.kaggle.com/competitions/home-credit-default-risk
- **License**: Kaggle Competition Rules
- **Access**: Requires Kaggle account and competition rules acceptance

## Description
Predict loan repayment ability for 307K+ applicants using multi-table financial data. Contains application details, credit bureau records, past loan histories, and installment payment records.

## Download Instructions
```powershell
# Set Kaggle credentials
$env:KAGGLE_USERNAME = "your_username"
$env:KAGGLE_KEY = "your_api_key"

# Download (~1.7 GB compressed)
kaggle competitions download -c home-credit-default-risk -p home-credit-default-risk/raw/

# Extract
Expand-Archive -Path "home-credit-default-risk/raw/home-credit-default-risk.zip" -DestinationPath "home-credit-default-risk/raw/"
```

## Target Variable
`TARGET` (in `application_train.csv`): 0 = Repaid, 1 = Default

## Key Files
- `application_train.csv` — 307,511 rows × 122 columns (main training table)
- `bureau.csv` — Credit Bureau data for each client
- `previous_application.csv` — Previous Home Credit loan applications
- `installments_payments.csv` — Payment history

## Notes
- Multi-table structure requires joining and aggregation for feature engineering
- 60+ columns have >50% missing values
- May be overly complex for HW1 — consider using only `application_train.csv`
