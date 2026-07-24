PREVIEW = True

def rectangles(rows: list[str]) -> int:
    rect_count = 0
    for r, row in enumerate(rows[:-1]):
        for left_edge, cell in enumerate(row[:-1]):
            preview(rows, [r], [left_edge])
            if cell == "+":
                for right_edge, next_cell in enumerate(row[left_edge+1:], start=left_edge+1):
                    preview(rows, [r], [left_edge, right_edge])
                    if next_cell in [" ", "|"]:
                        break
                    if next_cell == "+":
                        for n_r, next_row in enumerate(rows[r+1:], start=r+1):
                            preview(rows, [r, n_r], [left_edge, right_edge])
                            if next_row[left_edge] in [" ", "-"] or next_row[right_edge] in [" ", "-"]:
                                break
                            if next_row[left_edge] == "+" and next_row[right_edge] == "+":
                                bottom = True
                                for bottom_edge, bottom_cell in enumerate(next_row[left_edge+1:right_edge], start=left_edge+1):
                                    preview(rows, [r, n_r], [left_edge, right_edge], bottom_edge)
                                    if bottom_cell not in ["-", "+"]:
                                        bottom = False
                                        break
                                if bottom:
                                    rect_count += 1
    return rect_count


def preview(grid, target_rows, target_columns_top, target_column_bottom = -1):
    if not PREVIEW:
        return
    print("".join([" " if cell not in target_columns_top else "v" for cell in range(len(grid[0]))]))
    for r, row in enumerate(grid):
        if r in target_rows:
            print(row + " <")
        else:
            print(row)
    print("".join([" " if cell != target_column_bottom else "^" for cell in range(len(grid[0]))]))
