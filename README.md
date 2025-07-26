# Telco Customer Churn Data Pipeline

## 📌 Overview
This project demonstrates a simple ETL pipeline using **Python**, **Bash**, and **AWS S3**.  
The pipeline automatically:
1. **Extracts** the Telco Customer Churn dataset directly from **Kaggle**.
2. **Transforms & Cleans** the dataset (handling missing values, trimming strings, adding analytical columns).
3. **Loads** the cleaned dataset into an **AWS S3** bucket for further analytics.

---

## 🚀 Project Structure

telco-data-project/
  
data/  
  raw/              # Raw dataset downloaded from Kaggle  
  processed/        # Cleaned dataset after transformation  

scripts/  
  clean_data.py     # Cleans and processes the dataset  
  upload_to_s3.py   # Uploads processed data to AWS S3  

aws_keys/           # Stores AWS credentials (excluded from GitHub)  

.gitignore  
run_all.sh          # Orchestrates the entire workflow  
README.md  

 
---

## 🔧 Requirements
- Python 3
- pandas
- boto3 (for AWS integration)
- Kaggle API (`kaggle` CLI)

---

## ▶️ Usage

### 1️⃣ **Run the full pipeline**
 
chmod +x run_all.sh
./run_all.sh
This script:

Downloads the dataset from Kaggle.

Cleans and transforms it.

Saves the processed file to data/processed/cleaned_telco.csv.

2️⃣ Upload to AWS S3 (Optional)
 
./scripts/upload_to_s3.py
Requires aws_keys/aws_credentials.csv containing your AWS keys.

☁️ AWS Integration
The cleaned dataset is automatically uploaded to your AWS S3 bucket using boto3.

You can later connect AWS Athena or Power BI directly to your S3 data for analytics.

📊 Output
The final dataset is stored in:

 
data/processed/cleaned_telco.csv
And also available in your configured S3 bucket.

✅ Key Features
✅ Automated data extraction from Kaggle.

✅ Automated data cleaning with additional analytical features.

✅ Automated data upload to AWS S3 for cloud analytics.

 
