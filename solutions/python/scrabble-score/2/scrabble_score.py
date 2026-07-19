SCORE_LOOKUP =("", "AEIOULNRST", "DG", "BCMP", "FHVWY", "K", "", "", "JX", "", "QZ")


def score(word: str) -> int:
    """Compute the scrabble score of the input."""
    return sum(point_value for letter in word.upper() 
                for point_value, letters in enumerate(SCORE_LOOKUP) 
                if letters and letter in letters)
