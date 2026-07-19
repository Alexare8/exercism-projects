from string import ascii_uppercase


def rows(letter: str) -> list[str]:
    "Returns a diamond pattern"
    max_letter = ord(letter) - 64
    text_art = []

    for i, char in enumerate(ascii_uppercase[:max_letter], 0):
        if char == "A":
            text_art.append("A".center(max_letter * 2 - 1))
        else:
            text_art.append(f"{char}{' ' * (2 * i - 1)}{char}".center(max_letter * 2 - 1))

    text_art.extend(reversed(text_art[:-1]))
    return text_art
