def line_up(name: str, number: int) -> str:
    """Greet customers with their name and number in a sentence."""
    return f"{name}, you are the {ordinal(number)} customer we serve today. Thank you!"


def ordinal(number: int) -> str:
    """Return the ordinal string version of a natural number."""
    suffix = "th"
    match number % 10:
        case 1:
            if not number % 100 == 11:
                suffix = "st"
        case 2:
            if not number % 100 == 12:
                suffix = "nd"
        case 3:
            if not number % 100 == 13:
                suffix = "rd"
    return f"{number}{suffix}"
