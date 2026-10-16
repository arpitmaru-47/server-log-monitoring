import os
from pathlib import Path
from datetime import datetime 

report_dir = Path("reports")
report_dir.mkdir(exist_ok=True)

environment = os.getenv("APP_ENV", "not-set")
current_dir = Path.cwd() 

report = report_dir / "system_reports.txt"

with report.open("w", encoding="utf-8") as file:
    file.write(f"Generated: {datetime.now()}\n")
    file.write(f"Current directory: {current_dir}\n")
    file.write(f"Application environment: {environment}\n")

print(f"Report created: {report}")