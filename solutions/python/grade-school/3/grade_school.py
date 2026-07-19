from collections import defaultdict
from bisect import insort


class School:
    def __init__(self):
        self.students = set()
        self.grades = defaultdict(list)
        self.log = []

    def add_student(self, name: str, grade: int) -> None:
        if name in self.students:
            self.log.append(False)
        else:
            self.students.add(name)
            insort(self.grades[grade], name)
            self.log.append(True)

    def roster(self) -> list[str]:
        ros = []
        for grade_number in sorted(self.grades):
            for student in self.grade(grade_number):
                ros.append(student)
        return ros

    def grade(self, grade_number: int) -> list[str]:
        return self.grades[grade_number]

    def added(self) -> list[bool]:
        return self.log
