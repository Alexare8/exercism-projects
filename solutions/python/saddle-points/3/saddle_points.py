def saddle_points(matrix: list[list]) -> dict:
    """Identifies the saddle points in a given matrix."""

    points = []
    if not matrix:
        return points

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")

    matrix_rot = list(zip(*matrix))

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            v = matrix[y][x]
            if v == max(matrix[y]) and v == min(matrix_rot[x]):
                points.append({"row": y + 1, "column": x + 1})

    return points