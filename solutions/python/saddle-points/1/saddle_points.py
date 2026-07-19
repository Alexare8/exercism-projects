def saddle_points(matrix):
    if any(1 for row in matrix if len(row) != len(matrix[0])):
        raise ValueError("irregular matrix")
    
    output = []
    tallest = []
    for i, row in enumerate(matrix):
        for j, tree in enumerate(row):
            if not any(1 for other_tree in row if other_tree > tree):
                tallest.append((tree, i, j))

    for tree in tallest:
        valid = True
        for row in matrix:
            if row[tree[2]] < tree[0]:
                valid = False
        if valid == True:
            output.append({"row": tree[1] + 1, "column": tree[2] + 1})
        
    return output