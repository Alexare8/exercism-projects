class School:
    def __init__(self):
        self.students = []
        self.log = []

    def add_student(self, name: str, grade: int) -> None:
        while len(self.students) < grade + 1:
            self.students.append([])
        if name in self.roster():
            self.log.append(False)
        else:
            self.students[grade].append(name)
            self.log.append(True)

    def roster(self) -> list[str]:
        ros = []
        for i in range(len(self.students)):
            for student in self.grade(i):
                ros.append(student)
        return ros

    def grade(self, grade_number: int) -> list[str]:
        if not self.students:
            return []
        return sorted(self.students[grade_number])

    def added(self) -> list[bool]:
        return self.log
