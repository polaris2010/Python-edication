from enum import Enum
from typing import List

class Subject(Enum):
    MATH = 'Математика'
    RUSSIAN_LANG = 'Русский Язык'
    FOREAN_LANG = 'Английский Язык'

class Human:
    def __init__(self, name: str, last_name: str):
        self.name = name
        self.last_name = last_name

class Class:
    def __init__(self, grade: int, letter: str, homeroom_teacher, students=None):
        self._grade = grade
        self._letter = letter
        self._homeroom_teacher = homeroom_teacher
        self._students = students if students is not None else []

    def __iter__(self):
        sorted_students = sorted(self._students, key=lambda students: (students.last_name, students.name))
        return iter(sorted_students)

    def __getitem__(self, name: str):
        return [student for student in self._students if name in (student.name, student.last_name)]

class Student(Human):
    def __init__(self, name: str, last_name: str, school_class=None):
        super().__init__(name, last_name)
        self._class = school_class

    def set_class(self, school_class):
        self._class = school_class

    def get_class(self):
        return self._class

class Teacher(Human):
    def __init__(self, name: str, last_name: str, subjects: List[Subject], homeroom_class=None):
        super().__init__(name, last_name)
        self._subjects = subjects
        self._homeroom_class = homeroom_class

    def set_class(self, school_class):
        self._homeroom_class = school_class

    def get_class(self):
        return self._homeroom_class

classroom_teacher = Teacher("Иван", "Иванов", [Subject.MATH, Subject.RUSSIAN_LANG])
student1 = Student("Петр", "Петров", "10A")
student2 = Student("Иван", "Сидоров", "10A")
school_class = Class(10, "A", classroom_teacher, [student1, student2])

# Пример использования методов класса Class
print("Все ученики с фамилией или именем начинающимся на 'Пет':")
print(school_class["Пет"])
print("Список всех учеников:")
for student in school_class:
    print(student.name, student.last_name)
