def egg_count(display_value: int) -> int:
    """Determine the number of eggs in Eliud's coop."""
    return bin(display_value).count('1')