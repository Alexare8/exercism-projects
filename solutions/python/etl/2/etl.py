def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:
    """Convert old dict (score, [letters]) to new dict (letter, score)."""
    return {letter.lower(): score for score in legacy_data for letter in legacy_data[score]}
