from pathlib import Path
import random


DATA_DIR = Path(__file__).resolve().parent / "data"
STUDENTS_FILE = DATA_DIR / "students.txt"
REPORT_FILE = DATA_DIR / "report.txt"
LOG_FILE = DATA_DIR / "activity.log"


def ensure_data_dir():
    DATA_DIR.mkdir(exist_ok=True)

# Generate_data_file
def load_students():
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