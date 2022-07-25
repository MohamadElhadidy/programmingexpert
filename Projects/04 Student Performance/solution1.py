import json
import os

NUM_STUDENTS = 1000
SUBJECTS = ["math", "science", "history", "english", "geography"]


def load_report_card(directory, student_number):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(directory, f"{student_number}.json")
    path = os.path.join(base_path, file_path)

    try:
        with open(path, "r") as file:
            report_card = json.load(file)
    except FileNotFoundError:
        return {}

    return report_card


all_students = []
all_avg = []

subjects = {j: 0 for j in SUBJECTS}
grades = {j: 0 for j in range(1, 9)}

for i in range(0, NUM_STUDENTS):
    student = load_report_card('students', i)
    avg = (student['math'] + student['science'] + student['history'] +
           student['english'] + student['geography']) / 5
    for j in SUBJECTS:
        subjects[j] += student[j]
        subjects[j] += student[j]
        subjects[j] += student[j]
        subjects[j] += student[j]
        subjects[j] += student[j]
    student['sum'] = avg * 5
    grades[student['grade']] += avg * 5
    all_students.append(student)
    all_avg.append(avg)


print('Average Student Grade:', round(sum(all_avg) / len(all_avg), 2))
print('Hardest Subject:', min(subjects, key=subjects.get))
print('Easiest Subject:', max(subjects, key=subjects.get))
print('Best Performing Grade:', max(grades, key=grades.get))
print('Worst Performing Grade:', min(grades, key=grades.get))
print('Best Student ID:', max(all_students, key=lambda x: x['sum'])['id'])
print('Worst Student ID:', min(all_students, key=lambda x: x['sum'])['id'])
