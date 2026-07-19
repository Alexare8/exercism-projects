def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:
    """Convert old (score, letters) dict to new (letter, score) dict."""
    return dict((letter.lower(), score) for score, letters in legacy_data.items() for letter in letters)
