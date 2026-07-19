from collections import Counter
import re


def count_words(sentence: str) -> dict[str: int]:
    """Returns a dictionary of each word used in the input sentence keyed to the number of times it appeared."""
    return Counter(re.findall(r"'*([a-z]*'?[a-z0-9]+)'*", sentence.lower()))
