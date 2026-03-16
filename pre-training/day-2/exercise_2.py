students = [
    {"name": "Alice", "scores": [88, 92, 79, 95], "subject": "Math"},
    {"name": "Bob", "scores": [70, 65, 80, 74], "subject": "Science"},
    {"name": "Carol", "scores": [95, 98, 91, 99], "subject": "English"},
    {"name": "David", "scores": [60, 72, 68, 75], "subject": "History"},
    {"name": "Eve", "scores": [85, 88, 90, 87], "subject": "Art"},
]


def calculate_average(scores):
    return sum(scores) / len(scores)


def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def class_topper(students):
    return max(students, key=lambda s: calculate_average(s["scores"]))


topper = class_topper(students)
print(f"Class topper: {topper['name']} with average score of {calculate_average(topper['scores']):.2f}")

sorted_students = sorted(students, key=lambda s: calculate_average(s["scores"]), reverse=True)
print("\nSorted students by average score:", sorted_students)

print(f"{'Name':<10} | {'Avg Score':>9} | {'Grade':>5}")
print("-" * 32)
for student in sorted_students:
    avg = calculate_average(student["scores"])
    grade = get_grade(avg)
    marker = " *** TOP ***" if student["name"] == topper["name"] else ""
    print(f"{student['name']:<10} | {avg:>9.2f} | {grade:>5}{marker}")
