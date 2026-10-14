import csv
import os
from datetime import datetime

import psutil

REPORT_DIR = "reports"
CSV_FILE = f"{REPORT_DIR}/system_report.csv"
HTML_FILE = f"{REPORT_DIR}/system_report.html"

os.makedirs(REPORT_DIR, exist_ok=True)

cpu_usage = psutil.cpu_percent(interval=1)
memory_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage('/').percent

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# CSV REPORT

with open(CSV_FILE, "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Metric", "Value"])

    writer.writerow(["Timestamp", timestamp])
    writer.writerow(["CPU Usage", f"{cpu_usage}%"])
    writer.writerow(["Memory Usage", f"{memory_usage}%"])
    writer.writerow(["Disk Usage", f"{disk_usage}%"])

# HTML REPORT

html_content = f"""
<!DOCTYPE html>
<html>
<head>

<title>System Health Report</title>

<style>

body {{
    font-family: Arial, sans-serif;
    margin: 40px;
}}

table {{
    border-collapse: collapse;
    width: 50%;
}}

th, td {{
    border: 1px solid #ddd;
    padding: 10px;
}}

th {{
    background-color: #0078D7;
    color: white;
}}

</style>

</head>

<body>

<h1>System Health Report</h1>

<p>Generated: {timestamp}</p>

<table>

<tr>
<th>Metric</th>
<th>Value</th>
</tr>

<tr>
<td>CPU Usage</td>
<td>{cpu_usage}%</td>
</tr>

<tr>
<td>Memory Usage</td>
<td>{memory_usage}%</td>
</tr>

<tr>
<td>Disk Usage</td>
<td>{disk_usage}%</td>
</tr>

</table>

</body>

</html>
"""

with open(HTML_FILE, "w") as file:
    file.write(html_content)

print("\n=== REPORT GENERATED ===\n")

print(CSV_FILE)
print(HTML_FILE)