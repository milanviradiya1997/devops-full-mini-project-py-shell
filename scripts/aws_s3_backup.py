import os
import datetime

BUCKET = "milan-s3-bucket-demo"
SOURCE_DIR = "/var/log"
DATE = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")

cmd = f"aws s3 sync {SOURCE_DIR} s3://{BUCKET}/logs/{DATE}/"
print("Running:", cmd)
os.system(cmd)

print("✅ Logs backed up to S3")