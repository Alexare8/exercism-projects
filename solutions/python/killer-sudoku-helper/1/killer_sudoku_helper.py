def combinations(target: int, size: int, exclude: list[int]) -> list[list[int]]:
    solutions: list[list[int]] = []
    for num in range(1, 10):
        if num in exclude:
            continue
        if num == target and size == 1:
            solutions.append([num])
        elif num < target and size > 1:
            results = combinations(target - num, size - 1, exclude + [num])
            for result in results:
                full_result = sorted(result + [num])
                if not full_result in solutions:
                    solutions.append(full_result)
    return solutions
