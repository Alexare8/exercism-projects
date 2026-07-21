def tick(matrix: list[list[int]]) -> list[list[int]]:
    """Update a Game of Life matrix by one generation."""
    return GameOfLife(matrix).tick()


class GameOfLife:

    NEIGHBOR_OFFSETS = list((x, y) for x in [-1, 1, 0] for y in [-1, 1, 0] if x or y)

    def __init__(self, matrix: list[list[int]]) -> None:
        self.matrix = matrix

    def tick(self) -> list[list[int]]:
        """Step forward one generation."""
        new_matrix = []
        for row_index, row in enumerate(self.matrix):
            current_row = []
            for col_index, cell in enumerate(row):
                neighbors = self.count_neighbors(row_index, col_index)
                if neighbors == 3 or cell == 1 and neighbors == 2:
                    current_row.append(1)
                else:
                    current_row.append(0)
            new_matrix.append(current_row)
        return new_matrix

    def count_neighbors(self, row: int, column: int) -> int:
        """Count the number of living neighbors of a cell."""
        return sum(self.check_cell(row + row_offset, column + col_offset) for row_offset, col_offset in self.NEIGHBOR_OFFSETS)

    def check_cell(self, row: int, column: int) -> int:
        """Check the status of a single cell in the Game of Life matrix."""
        if 0 <= row < len(self.matrix) and 0 <= column < len(self.matrix):
            return self.matrix[row][column]
        return 0
