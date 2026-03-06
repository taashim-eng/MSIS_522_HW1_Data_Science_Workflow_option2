# Give Me Some Credit (Kaggle)

## Provenance
- **Source**: Kaggle Competition
- **URL**: https://www.kaggle.com/competitions/GiveMeSomeCredit
- **License**: Kaggle Competition Rules
- **Access**: Requires Kaggle account and competition rules acceptance

## Description
Predict the probability that a borrower will experience financial distress in the next 2 years. Contains ~150,000 rows with 10 financial features.

## Download Instructions
```powershell
# Set Kaggle credentials
$env:KAGGLE_USERNAME = "your_username"
$env:KAGGLE_KEY = "your_api_key"

# Download
kaggle competitions download -c GiveMeSomeCredit -p give-me-some-credit/raw/

# Extract
Expand-Archive -Path "give-me-some-credit/raw/GiveMeSomeCredit.zip" -DestinationPath "give-me-some-credit/raw/"
```

## Target Variable
`SeriousDlqin2yrs`: 0 = No distress, 1 = Financial distress within 2 years

## Key Features
- `RevolvingUtilizationOfUnsecuredLines` — Credit utilization ratio
- `age` — Borrower age
- `DebtRatio` — Monthly debt / gross income
- `MonthlyIncome` — Borrower's monthly income (~29K missing)
- `NumberOfDependents` — Number of dependents (~3.9K missing)

## Preprocessing Notes
- Impute `MonthlyIncome` with median
- Impute `NumberOfDependents` with 0 (mode)
- Clip extreme outliers in `RevolvingUtilizationOfUnsecuredLines` (some > 1.0)
