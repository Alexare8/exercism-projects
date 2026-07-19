def abbreviate(words: str) -> str:
    """Returns an ancronym of the input."""
    word_list = words.replace("-", " ").replace("_", "").split()
    return "".join(list(word[0].upper() for word in word_list))
