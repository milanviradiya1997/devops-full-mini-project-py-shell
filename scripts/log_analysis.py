log_file = "/var/log/messages"

error_count = 0
keyword = "error"

with open(log_file, "r", errors="ignore") as f:
    for line in f:
        if keyword.lower() in line.lower():
            error_count += 1

print(f"Total '{keyword}' occurrences:", error_count)

if error_count > 10:
    print("⚠️ High error rate detected")
else:
    print("✅ System looks healthy")
