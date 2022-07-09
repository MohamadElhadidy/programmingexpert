class Student:
    all_students = 0
    all_grades = 0
    students = []

    def __init__(self, name, grade):
        if grade < 0 or grade > 100:
            raise ValueError('')
        self.name = name
        self._grade = grade
        Student.all_students += 1
        Student.all_grades += grade
        Student.students.append(self)

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        if grade < 0 or grade > 100:
            raise ValueError('')
        self._grade = grade

    @classmethod
    def calculate_average_grade(cls, students):
        grade = 0
        for student in students:
            grade += student.grade
        avg = grade / len(students)
        return round(avg)

    @classmethod
    def get_average_grade(cls):
        if cls.all_students == 0:
            return -1
        return round(cls.all_grades / cls.all_students)

    @classmethod
    def get_best_student(cls):
        def sort(e):
            return e.grade
        if cls.all_students == 0:
            return None
        best_students = sorted(cls.students, reverse=True, key=sort)
        return best_students[0]
