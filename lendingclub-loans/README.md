# Lending Club Loans 2007-2020 (Kaggle)

## Provenance
- **Source**: Kaggle
- **URL**: https://www.kaggle.com/datasets/ethon0426/lending-club-20072020q1
- **License**: CC0 Public Domain
- **Access**: Requires Kaggle account

## Description
Peer-to-peer lending records for ~2.9 million loans issued through LendingClub from 2007 to 2020 Q1. Contains 151 features covering borrower profiles, loan details, FICO scores, and payment outcomes.

## Download Instructions
```powershell
# Set Kaggle credentials
$env:KAGGLE_USERNAME = "your_username"
$env:KAGGLE_KEY = "your_api_key"

# Download (~640 MB)
kaggle datasets download -d ethon0426/lending-club-20072020q1 -p lendingclub-loans/raw/

# Extract
Expand-Archive -Path "lendingclub-loans/raw/lending-club-20072020q1.zip" -DestinationPath "lendingclub-loans/raw/"
```

## Target Variable
`loan_status` — Map: "Charged Off" = 1 (default), "Fully Paid" = 0 (no default)  
Filter to only "Fully Paid" and "Charged Off" rows (exclude "Current", "In Grace Period", etc.)

## Key Features
- `loan_amnt`, `int_rate`, `annual_inc`, `dti`, `delinq_2yrs`
- `fico_range_low`, `fico_range_high`, `open_acc`, `pub_rec`
- `purpose`, `addr_state`, `emp_length`

## Notes
- Very large dataset — subsample for HW1 (e.g., 50K rows)
- 151 columns require significant feature selection
- `addr_state` and `zip_code` (3-digit) may be quasi-identifiers — consider redaction
- Substantial missing values across many columns
