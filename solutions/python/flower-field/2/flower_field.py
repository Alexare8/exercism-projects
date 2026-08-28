def annotate(garden: list[str]) -> list[str]:
    if garden in {[], [""]}:
        return garden
    for row in garden:
        if len(row) != len(garden[0]) or not all(char in {" ", "*"} for char in row):
            raise ValueError("The board is invalid with current input.")

    height = len(garden)
    width = len(garden[0])
    annotated_garden: list[str] = []

    for x, row in enumerate(garden):
        annotated_row = ""
        for y, cell in enumerate(row):
            if cell == "*":
                annotated_row += "*"
                continue
            neighbors = get_neighbors(x, y, height, width)
            flower_count = sum(1 for x, y in neighbors if garden[x][y] == "*")
            if flower_count == 0:
                annotated_row += " "
                continue
            annotated_row += str(flower_count)
        annotated_garden.append(annotated_row)

    return annotated_garden


def get_neighbors(x: int, y: int, height: int, width: int) -> list[tuple[int, int]]:
    """List the neighbors of (X, Y) on a grid of given height and width."""
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    return [
        (dx + x, dy + y)
        for dx, dy in offsets
        if 0 <= dx + x < height and 0 <= dy + y < width
    ]
