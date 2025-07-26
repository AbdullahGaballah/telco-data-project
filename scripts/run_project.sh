echo "[Step 1] Running data cleaning script..."
python3 ./scripts/clean_data.py

echo "[Step 2] Uploading file to AWS S3..."
python3 ./scripts/upload_to_s3.py

echo "[Step 3] Done ✅"
