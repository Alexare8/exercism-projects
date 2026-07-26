def rectangles(rows: list[str]) -> int:
    """Count the complete rectangles."""
    rect_count = 0
    for r, row in enumerate(rows[:-1]):
        for left_edge, cell in enumerate(row[:-1]):
            if cell == "+":
                for right_edge, next_cell in enumerate(row[left_edge+1:], start=left_edge+1):
                    if next_cell in {" ", "|"}:
                        break
                    if next_cell == "+":
                        for next_row in rows[r+1:]:
                            if next_row[left_edge] in {" ", "-"} or next_row[right_edge] in {" ", "-"}:
                                break
                            if next_row[left_edge] == "+" and next_row[right_edge] == "+":
                                bottom = True
                                for bottom_cell in next_row[left_edge+1:right_edge]:
                                    if bottom_cell not in {"-", "+"}:
                                        bottom = False
                                        break
                                if bottom:
                                    rect_count += 1
    return rect_count
