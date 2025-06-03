import re
from collections import Counter


with open("auth.log", "r") as file:
    log_lines = file.readlines()
failed_ips = []

for line in log_lines:
    if "Failed password" in line:
        match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
        if match:
            failed_ips.append(match.group(1))

ip_counts = Counter(failed_ips)

print("Top 5 IPs ayant échoué :")
for ip, count in ip_counts.most_common(5):
    print(f"{ip}: {count} tentatives échouées")
