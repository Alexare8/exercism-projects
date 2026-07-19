from string import ascii_lowercase
ENCODING = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])


def encode(plain_text: str) -> str:
    """Encode a string with the atbash cipher into 5-character segments."""
    message = atbash(plain_text)
    return " ".join(message[index:index+5] for index in range(0, len(message), 5))

def decode(ciphered_text: str) -> str:
    """Decode atbash cipher text"""
    return atbash(ciphered_text)

def atbash(text: str) -> str:
    """Apply the atbash substitution cipher"""
    return normalize(text).translate(ENCODING)

def normalize(text: str) -> str:
    """Remove non-alphanumeric characters and casefold"""
    return "".join(char for char in text.replace(" ", "").casefold() if char.isalnum())