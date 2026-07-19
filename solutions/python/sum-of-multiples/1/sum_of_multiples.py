def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    """Calculate the energy earned by collecting magic items."""
    return sum(set(factor for item in multiples if item != 0 for factor in range(item, limit, item)))
