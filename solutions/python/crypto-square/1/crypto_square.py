from math import ceil, sqrt


def cipher_text(plain_text: str) -> str:
    """Encode text with a square cipher."""
    clean_text = normalize(plain_text)
    if not clean_text:
        return ''
    edge_length = ceil(sqrt(len(clean_text)))
    clean_text = clean_text.ljust(edge_length * ceil(len(clean_text) / edge_length), ' ')
    square = [clean_text[i : i + edge_length] for i in range(0, len(clean_text), edge_length)]
    other_square = [''.join(column) for column in zip(*square)]
    return ' '.join(other_square)


def normalize(text: str) -> str:
    """Remove spaces and punctuation then casefold."""
    return ''.join(char for char in text if char.isalnum()).casefold()