from string import ascii_lowercase
ENCODING = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])


def encode(plain_text: str) -> str:
    """Encode a string with the atbash cipher."""
    message = "".join(char for char in plain_text.replace(" ", "").lower() if char.isalnum()).translate(ENCODING)
    return " ".join(message[index:index+5] for index in range(0, len(message), 5))

def decode(ciphered_text: str) -> str:
    """Decode atbash cipher text"""
    return str("".join(chr(219 - ord(char)) if char.isalpha() else char for char in ciphered_text if char != " "))
