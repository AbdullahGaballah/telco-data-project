#!/bin/bash

set -e

KAGGLE_DATASET="blastchar/telco-customer-churn"
ZIP_PATH="./data/raw/telco-customer-churn.zip"
EXTRACT_DIR="./data/raw"

mkdir -p "$EXTRACT_DIR"

if [ ! -f "$ZIP_PATH" ]; then
    kaggle datasets download -d "$KAGGLE_DATASET" -p "$EXTRACT_DIR"
else
    echo "File already exists: $ZIP_PATH"
fi

if ! ls "$EXTRACT_DIR" | grep -qi '\.csv'; then
    unzip -o "$ZIP_PATH" -d "$EXTRACT_DIR"
else
    echo "CSV already extracted in $EXTRACT_DIR"
fi
