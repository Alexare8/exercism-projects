SCORE_LOOKUP = {1: "AEIOULNRST", 2: "DG", 3: "BCMP", 4: "FHVWY", 5: "K", 8: "JX", 10: "QZ"}


def score(word: str) -> int:
    """Compute the scrabble score of the input."""
    return sum(point_value for letter in word for point_value, letters in SCORE_LOOKUP.items() if letter.upper() in letters)
