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