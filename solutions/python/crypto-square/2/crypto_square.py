from math import ceil, sqrt


def cipher_text(plain_text: str) -> str:
    """Encode text with a square cipher."""
    clean_text = normalize(plain_text)
    if not clean_text:
        return ''
    matrix = create_matrix(clean_text)
    rot_matrix = [''.join(column) for column in zip(*matrix)]
    return ' '.join(rot_matrix)


def normalize(text: str) -> str:
    """Remove spaces and punctuation then casefold."""
    return ''.join(char for char in text if char.isalnum()).casefold()


def create_matrix(input_str: str) -> list[str]:
    """Turn a string into a matrix, as square as possible."""
    edge_length = ceil(sqrt(len(input_str)))
    input_str = input_str.ljust(edge_length * ceil(len(input_str) / edge_length), ' ')
    return [input_str[i : i + edge_length] for i in range(0, len(input_str), edge_length)]