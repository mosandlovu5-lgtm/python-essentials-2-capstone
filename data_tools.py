from pathlib import Path
from datetime import datetime
import random


DATA_DIR = Path(__file__).resolve().parent / "data"
STUDENTS_FILE = DATA_DIR / "students.txt"
REPORT_FILE = DATA_DIR / "report.txt"
LOG_FILE = DATA_DIR / "activity.log"


def ensure_data_dir():
    DATA_DIR.mkdir(exist_ok=True)

# Generate_data_file
def load_students():
    from datetime import datetime


def export_report(text):
    ensure_data_dir()

    with REPORT_FILE.open("w", encoding="utf-8") as file:
        file.write(text)

    log_event("Exported report.txt")
    return REPORT_FILE


def log_event(message):
    ensure_data_dir()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with LOG_FILE.open("a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")
        log_event("Generated messy sample student data")
    if not STUDENTS_FILE.exists():
        raise FileNotFoundError(
            "No data file yet. Choose option 1 first."
        )

    clean_records = []

    with STUDENTS_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(",")

            if len(parts) != 2:
                continue

            try:
                name = " ".join(parts[0].strip().lower().title().split())
                score = int(parts[1].strip())

                if name and 0 <= score <= 100:
                    clean_records.append((name, score))

            except ValueError:
                continue

    return clean_records   