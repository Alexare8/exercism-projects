def rectangles(rows: list[str]) -> int:
    """Count the complete rectangles."""
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
                    if next_row[left_edge] in {" ", "-"} or next_row[right_edge] in {" ", "-"}:
                        break
                    if next_row[left_edge] != "+" or next_row[right_edge] != "+":
                        continue
                    if all(cell in {"-", "+"} for cell in next_row[left_edge+1:right_edge]):
                        rect_count += 1

    return rect_count
