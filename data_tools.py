from pathlib import Path
import random


DATA_DIR = Path(__file__).resolve().parent / "data"
STUDENTS_FILE = DATA_DIR / "students.txt"
REPORT_FILE = DATA_DIR / "report.txt"
LOG_FILE = DATA_DIR / "activity.log"


def ensure_data_dir():
    DATA_DIR.mkdir(exist_ok=True)


def generate_data_file():
    ensure_data_dir()

    raw_names = [
        "  lebo molefe  ",
        "AISHA khan",
        "  thabo NKOSI",
        "zanele dlamini  ",
        "michael  smith",
        "  priya naidoo",
        "SIPHO  MASEKO",
        "nina williams",
        "  karabo tsotlhe",
        "JAMES brown",
    ]

    random.shuffle(raw_names)

    with STUDENTS_FILE.open("w", encoding="utf-8") as file:
        for name in raw_names:
            score = random.randint(35, 98)
            file.write(f" {name} , {score} \n")

    return STUDENTS_FILE