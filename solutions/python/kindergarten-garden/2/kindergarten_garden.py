from collections.abc import Iterable
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
            batches = list(batched(row, 2))
            cups.extend(batches[stu_index])
        return [PLANTS[cup] for cup in cups]


def batched(iter: Iterable, size):
        for i in range(0, len(iter), size):
            yield iter[i:i+size]