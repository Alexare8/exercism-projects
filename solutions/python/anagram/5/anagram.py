def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """Finds all anagrams of a given word in a list of candidates. Ignores case."""
    len_word = len(word)
    lower_word = word.lower()
    sorted_word = sorted(list(lower_word))
    return [cand for cand in candidates 
            if len(cand) == len_word
            and cand.lower() != lower_word
            and sorted(list(cand.lower())) == sorted_word]
