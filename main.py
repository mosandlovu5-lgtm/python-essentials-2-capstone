from analytics import (
    class_average,
    highest,
    lowest,
    make_grader,
    pass_rate,
    passing_students,
    score_preview,
)
from data_tools import export_report, generate_data_file, load_students, log_event
from models import HonoursStudent, Student
from reporting import date_report, environment_report


HONOURS_TOPICS = {
    "Lebo Molefe": "Learning analytics and student success"
}


def show_menu():
    print("\n===== STUDENT ANALYTICS TOOLKIT =====")
    print("1. Generate sample data file")
    print("2. Load & clean records from file")
    print("3. View all students")
    print("4. Analyse (averages, pass/fail, top student)")
    print("5. Filter students (generator)")
    print("6. Grade with a custom pass mark (closure)")
    print("7. Environment & date report")
    print("8. Export results to a file")
    print("9. Exit")


def build_objects(records):
    students = []

    for number, record in enumerate(records, start=1):
        name, score = record
        student_id = f"S{number}"

        if name in HONOURS_TOPICS:
            student = HonoursStudent(
                name,
                student_id,
                score,
                HONOURS_TOPICS[name]
            )
        else:
            student = Student(name, student_id, score)

        students.append(student)

    return students


def require_students(students):
    if students:
        return True

    print("No students loaded. Choose option 2 first.")
    return False


def analysis_text(students):
    average = class_average(students)
    top_student = highest(students)
    bottom_student = lowest(students)
    rate = pass_rate(students)

    return (
        "STUDENT ANALYSIS\n"
        f"Students loaded: {len(students)}\n"
        f"Class average: {average:.2f}\n"
        f"Pass rate: {rate:.1f}%\n"
        f"Top student: {top_student}\n"
        f"Lowest student: {bottom_student}\n"
        f"First scores via iterator: {score_preview(students)}"
    )


def run():
    students = []

    while True:
        show_menu()
        choice = input("Choose an option (1-9): ").strip()

        if choice == "1":
            path = generate_data_file()
            print(f"Created messy sample data: {path}")

        elif choice == "2":
            try:
                records = load_students()
                students = build_objects(records)
                print(f"Loaded {len(students)} clean student records.")
            except FileNotFoundError as error:
                print(error)

        elif choice == "3":
            if require_students(students):
                for student in students:
                    print(student)

        elif choice == "4":
            if require_students(students):
                print(analysis_text(students))
                log_event("Ran student analysis")

        elif choice == "5":
            if require_students(students):
                print("Passing students:")

                for student in passing_students(students):
                    print(student)

        elif choice == "6":
            if require_students(students):
                try:
                    pass_mark = int(
                        input("Enter a pass mark from 0 to 100: ")
                    )

                    if not 0 <= pass_mark <= 100:
                        raise ValueError

                except ValueError:
                    print("Please enter a whole number from 0 to 100.")
                    continue

                grader = make_grader(pass_mark)
                normal_grader = make_grader(50)

                for student in students:
                    result = grader(student.score)
                    print(
                        f"{student.name}: {result} "
                        f"at a pass mark of {pass_mark}"
                    )

                example_score = students[0].score

                print(
                    f"\nClosure comparison for score {example_score}:"
                )
                print(f"Pass mark 50: {normal_grader(example_score)}")
                print(
                    f"Pass mark {pass_mark}: "
                    f"{grader(example_score)}"
                )

        elif choice == "7":
            print()
            print(environment_report())
            print()
            print(date_report())

        elif choice == "8":
            if require_students(students):
                report = (
                    f"{analysis_text(students)}\n\n"
                    f"{environment_report()}\n\n"
                    f"{date_report()}\n"
                )

                path = export_report(report)
                print(f"Exported report to: {path}")

        elif choice == "9":
            log_event("Exited Student Analytics Toolkit")
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 9.")


if __name__ == "__main__":
    run()