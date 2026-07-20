OFFSETS = [-1, 0, 1]

def tick(matrix: list[list[int]]) -> list[list[int]]:
    """Update the Game of Life matrix by one generation."""
    new_matrix = []
    for row_index, row in enumerate(matrix):
        new_matrix.append([])
        for col_index, cell in enumerate(row):
            neighbors = count_neighbors(matrix, row_index, col_index)
            if (cell == 1 and 2 <= neighbors <= 3) or neighbors == 3:
                new_matrix[row_index].append(1)
            else:
                new_matrix[row_index].append(0)
    return new_matrix


def count_neighbors(matrix: list[list[int]], row: int, column: int) -> int:
    """Count the number of living neighbors of the cell at the given coordinate."""
    neighbors = 0
    for row_offset in OFFSETS:
        for col_offset in OFFSETS:
            if not(row_offset == 0 and col_offset == 0):
                neighbors += check_cell(matrix, row + row_offset, column + col_offset)
    return neighbors


def check_cell(matrix: list[list[int]], row: int, column: int) -> int:
    """Check the status of a single cell in the Game of Life matrix."""
    if 0 <= row < len(matrix) and 0 <= column < len(matrix):
        return matrix[row][column]
    return 0
