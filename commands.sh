#!/bin/bash
# ============================================================
# MSIS 522 HW1 — Dataset Download & Verification Commands
# Alternative Credit Scoring Project
# Generated: 2026-03-05
# ============================================================

BASE_DIR="Option 2 for the credit scoring"

# ============================================================
# Dataset 1: German Credit (UCI) — Direct Download
# ============================================================
echo ">>> Downloading German Credit dataset..."
mkdir -p "${BASE_DIR}/german-credit/raw"
curl -o "${BASE_DIR}/german-credit/raw/german.data" \
     "https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data"
curl -o "${BASE_DIR}/german-credit/raw/german.data-numeric" \
     "https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data-numeric"
curl -o "${BASE_DIR}/german-credit/raw/german.doc" \
     "https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.doc"

# ============================================================
# Dataset 2: Taiwan Credit (UCI) — Direct Download
# ============================================================
echo ">>> Downloading Taiwan Default of Credit Card Clients..."
mkdir -p "${BASE_DIR}/taiwan-credit/raw"
curl -Lo "${BASE_DIR}/taiwan-credit/raw/default_credit_card_clients.zip" \
     "https://archive.ics.uci.edu/static/public/350/default+of+credit+card+clients.zip"
cd "${BASE_DIR}/taiwan-credit/raw" && unzip -o default_credit_card_clients.zip && cd -

# ============================================================
# Dataset 3: FICO HELOC — Direct Download (GitHub mirror)
# ============================================================
echo ">>> Downloading FICO HELOC dataset..."
mkdir -p "${BASE_DIR}/fico-heloc/raw"
curl -o "${BASE_DIR}/fico-heloc/raw/heloc_dataset_v1.csv" \
     "https://raw.githubusercontent.com/benoitparis/explainable-challenge/master/heloc_dataset_v1.csv"

# ============================================================
# Dataset 4: Give Me Some Credit — Kaggle (requires credentials)
# ============================================================
echo ">>> Downloading Give Me Some Credit (Kaggle)..."
echo "    Requires: export KAGGLE_USERNAME=... KAGGLE_KEY=..."
mkdir -p "${BASE_DIR}/give-me-some-credit/raw"
# kaggle competitions download -c GiveMeSomeCredit -p "${BASE_DIR}/give-me-some-credit/raw/"

# ============================================================
# Dataset 5: Home Credit Default Risk — Kaggle (requires credentials)
# ============================================================
echo ">>> Downloading Home Credit Default Risk (Kaggle)..."
echo "    Requires: export KAGGLE_USERNAME=... KAGGLE_KEY=..."
mkdir -p "${BASE_DIR}/home-credit-default-risk/raw"
# kaggle competitions download -c home-credit-default-risk -p "${BASE_DIR}/home-credit-default-risk/raw/"

# ============================================================
# Dataset 6: LendingClub Loans — Kaggle (requires credentials)
# ============================================================
echo ">>> Downloading LendingClub Loans (Kaggle)..."
echo "    Requires: export KAGGLE_USERNAME=... KAGGLE_KEY=..."
mkdir -p "${BASE_DIR}/lendingclub-loans/raw"
# kaggle datasets download -d ethon0426/lending-club-20072020q1 -p "${BASE_DIR}/lendingclub-loans/raw/"

# ============================================================
# Verification: SHA-256 Checksums
# ============================================================
echo ""
echo ">>> Computing SHA-256 checksums..."
sha256sum "${BASE_DIR}/german-credit/raw/german.data"
sha256sum "${BASE_DIR}/german-credit/raw/german.data-numeric"
sha256sum "${BASE_DIR}/german-credit/raw/german.doc"
sha256sum "${BASE_DIR}/taiwan-credit/raw/default of credit card clients.xls"
sha256sum "${BASE_DIR}/fico-heloc/raw/heloc_dataset_v1.csv"

echo ">>> All downloads complete."
