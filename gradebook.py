from typing import List, Dict
from enum import Enum
import uuid


class AliveStatus(Enum):
    Deceased = 0
    Alive = 1


class Person:
    def __init__(self, f_name: str, l_name: str, dob: str):
        self.f_name = f_name
        self.l_name = l_name
        self.dob = dob
        self.alive = AliveStatus.Alive

    def update_first_name(self, f_name: str):
        self.f_name = f_name

    def update_last_name(self, l_name: str):
        self.l_name = l_name

    def update_dob(self, dob: str):
        self.dob = dob

    def update_status(self, alive: AliveStatus):
        self.alive = alive


class Instructor(Person):
    def __init__(self, f_name: str, l_name: str, dob: str):
        Person.__init__(self, f_name, l_name, dob)
        self.ins_id = f"Instructor_{uuid.uuid4()}"


class Student(Person):
    def __init__(self, f_name: str, l_name: str, dob: str):
        Person.__init__(self, f_name, l_name, dob)
        self.stud_id = f"Student_{uuid.uuid4()}"


class HighSchooler(Student):
    def __init__(self, first_name: str, last_name: str, dob: str):
        Student.__init__(self, first_name, last_name, dob)


class ZipCodeStudent(Student):
    def __init__(self, first_name: str, last_name: str, dob: str):
        Student.__init__(self, first_name, last_name, dob)


class GradeBook:
    pass


class Classroom:

    def __init__(self):
        self.students: Dict[str, Student] = {}
        self.instructors: Dict[str, Instructor] = {}

    def add_instructor(self, instructor: Instructor):
        self.instructors[instructor.ins_id] = instructor

    def remove_instructor(self, instructor: Instructor):
        if instructor.ins_id in self.instructors:
            del self.instructors[instructor.ins_id]

    def add_student(self, student: Student):
        self.students[student.stud_id] = student

    def remove_student(self, student):
        if student.student_id in self.students:
            del self.students[student.student_id]

    def print_instructors(self):
        for key, value in self.instructors.items():
            print(f"{key}: {value}")

    def print_students(self):
        for key, value in self.students.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    pass

rich = Person('rich', 'maiale', '112381')
Person.update_status(rich, 1)
print(rich.alive)