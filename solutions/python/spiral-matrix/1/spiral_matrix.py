def spiral_matrix(size: int) -> list[list[int]]:
    """Create a clockwise spiral matrix of increasing numbers."""
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    number = 1
    x, y = 0, 0
    step = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
    direction = 0
    while number <= size**2:
        matrix[x][y] = number
        next_x, next_y = x + step[direction][0], y + step[direction][1]
        if (
            any([next_x < 0, next_y < 0, next_x >= size, next_y >= size])
            or matrix[next_x][next_y] != 0
        ):
            direction = (direction + 1) % 4
        x, y = x + step[direction][0], y + step[direction][1]
        number += 1

    return matrix
