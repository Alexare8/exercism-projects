def triplets_with_sum(number: int) -> list[list]:
    """Find all pythagorean triplets that total a given sum."""
    triples = []
    for i in range(1, number // 3 + 1):
        i_i = i ** 2
        for j in range(i + 1, number // 2 + 1):
            k = number - i - j
            if i_i + j ** 2 == k ** 2:
                triples.append([i, j, k])
    return triples