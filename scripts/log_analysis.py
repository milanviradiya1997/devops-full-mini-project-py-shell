import os

LOG_FILES = [
    "/var/log/secure",
    "/var/log/cloud-init.log",
    "/var/log/dnf.log",
    "/var/log/nginx/error.log"
]

KEYWORD = "error"
total_errors = 0

for log_file in LOG_FILES:
    if os.path.exists(log_file):
        with open(log_file, "r", errors="ignore") as f:
            count = sum(1 for line in f if KEYWORD.lower() in line.lower())
            print(f"{log_file} → {count} errors")
            total_errors += count
    else:
        print(f"{log_file} → NOT FOUND (skipped)")

print("\nTotal error count:", total_errors)

if total_errors > 20:
    print("⚠️ ALERT: High error rate detected")
    exit(1)   # Jenkins will mark build unstable/fail
else:
    print("✅ System health looks OK")
