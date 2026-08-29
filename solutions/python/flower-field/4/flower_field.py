def annotate(garden: list[str]) -> list[str]:
    if not garden or garden == [""]:
        return garden
    for row in garden:
        if len(row) != len(garden[0]) or not all(char in {" ", "*"} for char in row):
            raise ValueError("The board is invalid with current input.")

    height = len(garden)
    width = len(garden[0])
    annotated_garden: list[str] = []

    for row_index, row in enumerate(garden):
        annotated_row: list[str] = []
        for column_index, cell in enumerate(row):
            if cell == "*":
                annotated_row.append("*")
                continue
            neighbors = get_neighbors(row_index, column_index, height, width)
            flower_count = sum(garden[x][y] == "*" for x, y in neighbors)
            if flower_count == 0:
                annotated_row.append(" ")
                continue
            annotated_row.append(str(flower_count))
        annotated_garden.append("".join(annotated_row))

    return annotated_garden


def get_neighbors(x: int, y: int, height: int, width: int) -> list[tuple[int, int]]:
    """List the neighbors of (X, Y) on a grid of given height and width."""
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    return [
        (dx + x, dy + y)
        for dx, dy in offsets
        if 0 <= dx + x < height and 0 <= dy + y < width
    ]
