from enum import Enum

class AliveStatus(Enum):
    Deceased = 0
    Alive = 1

class Person:
    def __init__(self, f_name, l_name, dob, alive):
        self.f_name = f_name

    def update_first_name(self, value):
        Person.f_name = self.new_name

        self.l_name = l_name

        self.dob = dob

        self.alive = AliveStatus




class Instructor:

class Student:

class ZipCodeStudent:

class Classroom:
    def students(self):




    def instructors(self):
