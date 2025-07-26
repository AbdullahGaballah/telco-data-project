#!/usr/bin/env python3

import pandas as pd
import os

def clean_data(input_path, output_path):
    df = pd.read_csv(input_path)

    df.columns = df.columns.str.strip()

    df.fillna(method='ffill', inplace=True)

    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

    df['HasInternetService'] = df['InternetService'].apply(lambda x: 'Yes' if x != 'No' else 'No')
    df['HasPhoneService'] = df['PhoneService'].apply(lambda x: 'Yes' if x == 'Yes' else 'No')

    def tenure_group(tenure):
        if tenure <= 12:
            return '0-1 Year'
        elif tenure <= 24:
            return '1-2 Years'
        elif tenure <= 48:
            return '2-4 Years'
        elif tenure <= 60:
            return '4-5 Years'
        else:
            return '5+ Years'

    df['TenureGroup'] = df['tenure'].apply(tenure_group)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

if __name__ == "__main__":
    input_file = './data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv'
    output_file = './data/processed/cleaned_telco.csv'
    clean_data(input_file, output_file)
