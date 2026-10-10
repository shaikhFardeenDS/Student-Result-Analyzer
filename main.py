"""
Student Result Analyzer
A beginner-friendly Python project that analyzes student marks.
"""

students = [
    {"name": "Aarav", "marks": [78, 85, 91]},
    {"name": "Priya", "marks": [92, 88, 95]},
    {"name": "Kabir", "marks": [65, 72, 70]},
    {"name": "Anaya", "marks": [84, 79, 88]},
    {"name": "Rohan", "marks": [55, 61, 58]},
]


def calculate_average(marks):
    """Return the average of a list of marks."""
    return sum(marks) / len(marks) if marks else 0


def grade_for(average):
    """Return a grade based on the average marks."""
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    return "Needs Improvement"


def show_report(student_list):
    """Print each student's average and grade."""
    print("\nSTUDENT RESULT REPORT")
    print("-" * 62)
    print(f"{'Name':<15}{'Subject 1':>10}{'Subject 2':>10}{'Subject 3':>10}{'Average':>10}{'Grade':>16}")
    print("-" * 62)

    for student in student_list:
        marks = student["marks"]
        average = calculate_average(marks)
        print(
            f"{student['name']:<15}"
            f"{marks[0]:>10}"
            f"{marks[1]:>10}"
            f"{marks[2]:>10}"
            f"{average:>10.1f}"
            f"{grade_for(average):>16}"
        )

    print("-" * 62)

    if student_list:
        top_student = max(student_list, key=lambda s: calculate_average(s["marks"]))
        class_average = sum(calculate_average(s["marks"]) for s in student_list) / len(student_list)
        print(f"Class average: {class_average:.1f}")
        print(
            f"Highest scorer: {top_student['name']} "
            f"({calculate_average(top_student['marks']):.1f} average)"
        )


if __name__ == "__main__":
    show_report(students)
