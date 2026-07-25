def rectangles(grid: list[str]) -> int:
    """Count the complete rectangles."""
    rect_count = 0
    corners = [(i, j) for i, row in enumerate(grid) for j, column in enumerate(row) if column == "+"]
    for top_left in corners[:-1]:
        for bottom_right in corners[1:]:
            if top_left[0] < bottom_right[0] and top_left[1] < bottom_right[1]:
                top_right = (top_left[0], bottom_right[1])
                bottom_left = (bottom_right[0], top_left[1])
                if (
                    all(corner in corners for corner in [top_left, top_right, bottom_left, bottom_right])
                    and check_row(grid, top_left, top_right)
                    and check_row(grid, bottom_left, bottom_right)
                    and check_side(grid, top_left, bottom_left)
                    and check_side(grid, top_right, bottom_right)
                ):
                    rect_count += 1
    return rect_count


def check_row(grid: list[str], left: tuple[int, int], right: tuple[int, int]) -> bool:
    """Check for a complete edge between two corners horizontally."""
    return not any(cell not in {"-", "+"} for cell in grid[left[0]][left[1] + 1:right[1]])


def check_side(grid: list[str], top: tuple[int, int], bottom: tuple[int, int]) -> bool:
    """Check for a complete edge between two corners vertically."""
    trasposed_grid = ["".join(row) for row in zip(*grid)]
    return not any(cell not in {"|", "+"} for cell in trasposed_grid[top[1]][top[0] + 1:bottom[0]])
