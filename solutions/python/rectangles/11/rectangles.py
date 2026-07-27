def rectangles(rows: list[str]) -> int:
    """Count the complete rectangles."""
    def check_rows(start_row: int, left_edge: int, right_edge: int) -> int:
        count = 0
        for next_row in rows[r+1:]:
            if next_row[left_edge] in {" ", "-"} or next_row[right_edge] in {" ", "-"}:
                break
            if next_row[left_edge] != "+" or next_row[right_edge] != "+":
                continue
            if all(cell in {"-", "+"} for cell in next_row[left_edge+1:right_edge]):
                count += 1
        return count

    rect_count = 0
    for r, row in enumerate(rows[:-1]):
        for left_edge, cell in enumerate(row[:-1]):
            if cell != "+":
                continue
            for right_edge, next_cell in enumerate(row[left_edge+1:], start=left_edge+1):
                if next_cell in {" ", "|"}:
                    break
                if next_cell != "+":
                    continue
                rect_count += check_rows(r + 1, left_edge, right_edge)
    return rect_count
