"""
    Define the Ward class.
"""

from datetime import datetime
from abc import ABC, abstractmethod

class Ward:
    def __init__(self, name):
        self._name = name
        self.ward_list = []

    def add_person(self, person):
        self.ward_list.append(person)

    def describe(self):
        print(f'Ward: {self._name}')
        for person in self.ward_list:
            person.describe()

    def count_doctor(self):
        return sum(1 for person in self.ward_list if isinstance(person, Doctor))

    def sort_age(self):
        if not self.ward_list:
            return

        old_list = self.ward_list.copy()
        new_list = []

        while old_list:
            min_person = old_list[0]
            min_index = 0
            for index, person in enumerate(old_list):
                if person._yob < min_person._yob:
                    min_person = person
                    min_index = index
            new_list.append(min_person)
            old_list.pop(min_index)

        self.ward_list = new_list

    def compute_average(self):
        age_list = []

        for person in self.ward_list:
            if isinstance(person, Teacher):
                age_list.append(datetime.now().year - person._yob)

        if age_list:
            return sum(age_list) / len(age_list)
        else:
            return 0

class Person(ABC):
    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass

class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        print(f'Name: {self._name}, Year of Birth: {self._yob}, Grade: {self._grade}')

class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self._subject = subject

    def describe(self):
        print(f'Name: {self._name}, Year of Birth: {self._yob}, Subject: {self._subject}')

class Doctor(Person):
    def __init__(self, name: str, yob: int, specialization: str):
        super().__init__(name, yob)
        self._specialization = specialization

    def describe(self):
        print(f'Name: {self._name}, Year of Birth: {self._yob}, Specialization: {self._specialization}')

def main():
    print('2(a)')
    student1 = Student(name="studentA", yob=2010, grade="7")
    student1.describe()

    teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
    teacher1.describe()

    doctor1 = Doctor(name="doctorA", yob=1945, specialization="Endocrinologists")
    doctor1.describe()

    print('2(b)')
    teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
    doctor2 = Doctor(name="doctorB", yob=1975, specialization="Cardiologists")

    ward1 = Ward("Ward1")

    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)

    ward1.describe()

    print('2(c)')
    print(ward1.count_doctor())

    print('2(d)')
    ward1.sort_age()
    ward1.describe()

    print('2(e)')
    print(ward1.compute_average())

if __name__ == "__main__":
    main()
