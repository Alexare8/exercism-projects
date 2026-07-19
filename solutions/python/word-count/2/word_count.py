import re


def count_words(sentence: str) -> dict[str: int]:
    """Returns a dictionary of each word used in the input sentence keyed to the number of times it appeared."""
    words = re.findall(r"([a-z0-9]+)(?![a-z'])|'([a-z]+'?[a-z]+)'|([a-z]+'[a-z]+)", sentence, flags=re.I)
    word_count = {}
    for word in words:
        if (word := "".join(word).lower()) in word_count:
            word_count[word] += 1
        else:
            word_count.update({word: 1})
    return word_count
