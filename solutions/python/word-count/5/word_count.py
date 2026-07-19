from collections import Counter
import re


def count_words(sentence: str) -> dict[str: int]:
    """Returns a dictionary of each word used in the input sentence keyed to the number of times it appeared."""
    words = re.findall(r"'*([a-z]*'?[a-z0-9]+)'*", sentence.lower())
    word_count = Counter()
    for word in words:
        word_count.update(["".join(word)])
    return word_count
