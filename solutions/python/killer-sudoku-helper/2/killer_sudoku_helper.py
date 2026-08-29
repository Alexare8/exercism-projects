from itertools import combinations as choose


def combinations(target: int, size: int, exclude: list[int]) -> list[list[int]]:
    excluded = set(exclude)
    available = [number for number in range(1, 10) if number not in excluded]

    return [
        list(numbers) for numbers in choose(available, size) if sum(numbers) == target
    ]
