class Matrix:
    def __init__(self, matrix_string: str) -> None:
        self.matrix = [[int(num) for num in line.split()] for line in matrix_string.split('\n')]

    def row(self, index: int) ->  list[int]:
        return self.matrix[index - 1]

    def column(self, index: int) ->  list[int]:
        return [list(col) for col in zip(*self.matrix)][index - 1]