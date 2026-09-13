from statistics import mean


def class_average(students):
    if not students:
        return None

    return mean(student.score for student in students)


def highest(students):
    return max(students, key=lambda student: student.score, default=None)


def lowest(students):
    return min(students, key=lambda student: student.score, default=None)


def pass_rate(students):
    if not students:
        return None

    passed_students = sum(student.has_passed() for student in students)
    return (passed_students / len(students)) * 100


def score_preview(students):
    scores = iter(student.score for student in students)
    preview = []

    for _ in range(2):
        try:
            preview.append(next(scores))
        except StopIteration:
            break

    return preview


def passing_students(students):
    for student in students:
        if student.has_passed():
            yield student


def make_grader(pass_mark):
    def grade(score):
        if score >= pass_mark:
            return "Pass"
        return "Fail"

    return grade