PLANTS = {'C': 'Clover', 'G': 'Grass', 'R': 'Radishes', 'V': 'Violets'}
DEFAULT_STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred',
                    'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']


class Garden:
    def __init__(self, diagram: str, students: list[str] = DEFAULT_STUDENTS) -> None:
        self.students = sorted(students)
        self.diagram = diagram.split('\n')

    def plants(self, student: str) -> list[str]:
        stu_index = self.students.index(student)
        cups: list[str] = []
        for row in self.diagram:
            cups.extend(row[stu_index * 2: stu_index * 2 + 2])
        return [PLANTS[cup] for cup in cups]
