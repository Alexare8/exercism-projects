def tick(matrix):
    """Update the Game of Life matrix by one generation."""
    new_matrix = [list(range(len(matrix[0]))) for _ in list(range(len(matrix)))]
    for row_index, row in enumerate(matrix):
        for col_index, cell in enumerate(row):
            neighbors = count_neighbors(matrix, row_index, col_index)
            if cell == 0 and neighbors == 3:
                new_matrix[row_index][col_index] = 1
            elif cell == 1 and (neighbors < 2 or neighbors > 3):
                new_matrix[row_index][col_index] = 0
            else:
                new_matrix[row_index][col_index] = cell
    return new_matrix


def count_neighbors(matrix, row, column) -> int:
    """Count the number of living neighbors of the cell at the given coordinate."""
    neighbors = 0
    offsets = [-1, 0, 1]
    for row_offset in offsets:
        for col_offset in offsets:
            neighbors += check_cell(matrix, row + row_offset, column + col_offset)
    neighbors -= matrix[row][column] # Counted the cell itself, needs to be removed from count
    return neighbors


def check_cell(matrix, row, column) -> int:
    """Check the status of a single cell in the Game of Life matrix."""
    if row < 0 or row > len(matrix) - 1:
        return 0
    if column < 0 or column > len(matrix[0]) - 1:
        return 0
    return matrix[row][column]
