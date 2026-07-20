SUFFIXES = {1: "st", 2: "nd", 3: "rd"}


def line_up(name: str, number: int) -> str:
    """Greet customers with their name and number in a sentence."""
    return f"{name}, you are the {ordinal(number)} customer we serve today. Thank you!"


def ordinal(number: int) -> str:
    """Return the ordinal string version of a natural number."""
    suffix = SUFFIXES.get(number % 10, "th")
    if number % 100 // 10 == 1:
        suffix = "th"
    return f"{number}{suffix}"
