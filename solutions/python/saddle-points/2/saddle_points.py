def saddle_points(matrix):
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")

    output = []
    for i, row in enumerate(matrix):
        for j, tree in enumerate(row):
            if all(tree <= row[j] for row in matrix) and all(tree >= column[i] for column in zip(*matrix)):
                output.append({"row": i + 1, "column": j + 1})

    return output