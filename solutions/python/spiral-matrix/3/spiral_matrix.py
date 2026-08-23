def spiral_matrix(size: int) -> list[list[int]]:
    """Create a counter-clockwise spiral matrix of increasing numbers."""
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    x, y = 0, 0
    step = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
    direction = 0
    for number in range(1, size**2 + 1):
        matrix[x][y] = number
        dx, dy = step[direction]
        next_x, next_y = x + dx, y + dy
        if (
            not (0 <= next_x < size and 0 <= next_y < size)
            or matrix[next_x][next_y] != 0
        ):
            direction = (direction + 1) % 4
            dx, dy = step[direction]
        x, y = x + dx, y + dy

    return matrix
