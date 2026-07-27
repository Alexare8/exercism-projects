def rectangles(rows: list[str]) -> int:
    """Count the complete rectangles."""
    def check_bottom_row(row: str, left_edge: int, right_edge: int) -> int:
        if row[left_edge] in {" ", "-"} or row[right_edge] in {" ", "-"}:
            return -1
        if row[left_edge] != "+" or row[right_edge] != "+":
            return 0
        if all(cell in {"-", "+"} for cell in row[left_edge+1:right_edge]):
            return 1
        return 0

    rect_count = 0
    for top_edge, row in enumerate(rows[:-1]):
        for left_edge, cell in enumerate(row[:-1]):
            if cell != "+":
                continue
            for right_edge, next_cell in enumerate(row[left_edge+1:], start=left_edge+1):
                if next_cell in {" ", "|"}:
                    break
                if next_cell != "+":
                    continue
                for next_row in rows[top_edge + 1:]:
                    if (row_status := check_bottom_row(next_row, left_edge, right_edge)) == -1:
                        break
                    rect_count += row_status
    return rect_count
