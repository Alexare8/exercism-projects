def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """Finds all anagrams of a given word in a list of candidates. Ignores case."""
    return [cand for cand in candidates 
                if sorted(list(cand.lower())) == sorted(list(word.lower())) 
                and cand.lower() != word.lower()]
