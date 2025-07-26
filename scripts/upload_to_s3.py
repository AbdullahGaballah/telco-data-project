#!/usr/bin/env python3

import boto3
import csv
import os

def read_aws_keys(filepath):
    import csv
    with open(filepath, mode='r', encoding='utf-8-sig') as f:  # utf-8-sig تزيل BOM تلقائي
        reader = csv.DictReader(f, delimiter=',')
        keys = next(reader)
        return keys['Access key ID'], keys['Secret access key']

KEY_FILE_PATH = os.path.expanduser('~/.aws_keys/aws_access_keys.csv')
ACCESS_KEY, SECRET_KEY = read_aws_keys(KEY_FILE_PATH)

BUCKET_NAME = 'telco-data-bucket'
FILE_PATH = './data/processed/cleaned_telco.csv'
OBJECT_NAME = 'cleaned_telco.csv'

def upload_to_s3():
    try:
        s3 = boto3.client('s3',
                          aws_access_key_id=ACCESS_KEY,
                          aws_secret_access_key=SECRET_KEY)
        s3.upload_file(FILE_PATH, BUCKET_NAME, OBJECT_NAME)
        print(f"File uploaded to S3 bucket '{BUCKET_NAME}' as '{OBJECT_NAME}'")
    except Exception as e:
        print("Upload failed:", e)

if __name__ == '__main__':
    upload_to_s3()
