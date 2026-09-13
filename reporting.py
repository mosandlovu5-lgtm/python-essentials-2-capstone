from pathlib import Path
import os
import platform
from datetime import date, datetime
import calendar

def environment_report():
    data_file = Path(__file__).resolve().parent / "data" / "students.txt"

    file_exists = data_file.exists()

    if file_exists:
        file_size = data_file.stat().st_size
    else:
        file_size = 0

    return (
        "ENVIRONMENT REPORT\n"
        f"Operating system: {platform.system()} {platform.release()}\n"
        f"Python version: {platform.python_version()}\n"
        f"Working directory: {os.getcwd()}\n"
        f"Students file exists: {file_exists}\n"
        f"Students file size: {file_size} bytes"
    )

def date_report():
    today = date.today()

    target_date = date(today.year, 12, 31)

    if target_date < today:
        target_date = date(today.year + 1, 12, 31)

    days_in_month = calendar.monthrange(today.year, today.month)[1]

    return (
        "DATE REPORT\n"
        f"Today: {today.strftime('%A, %d %B %Y')}\n"
        f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"Days until {target_date}: {(target_date - today).days}\n"
        f"Leap year: {calendar.isleap(today.year)}\n"
        f"Days in this month: {days_in_month}"
    )