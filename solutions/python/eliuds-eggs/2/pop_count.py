def egg_count(display_value: int) -> int:
    """Determine the number of eggs in Eliud's coop."""
    eggs = 0
    while display_value:
        eggs += display_value % 2
        display_value >>= 1
    return eggs