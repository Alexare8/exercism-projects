from secrets import randbelow
from itertools import cycle
from typing import Optional, Generator


class Cipher:
    """Encode or decode using a substitution cipher."""
    ENCODE = 1
    DECODE = -1
    ORD_OFFSET = 97
    ALPHABET_LENGTH = 26

    def __init__(self, key: Optional[str] = None) -> None:
        self.key = key or self.random_key(key_length = 100)
        
    def encode(self, text: str, direction: int = ENCODE) -> str:
        """Encode a plaintext string."""
        return ''.join(chr(((direction * key + letter) % self.ALPHABET_LENGTH) + self.ORD_OFFSET)
                       for letter, key in zip(self.ordify(text), cycle(self.ordify(self.key))))

    def decode(self, text: str) -> str:
        """Decode an encoded string."""
        return self.encode(text, self.DECODE)

    def ordify(self, text: str) -> Generator[int, None, None]:
        """Represent a string as an int offset from a = 0."""
        for letter in text:
            yield ord(letter) - self.ORD_OFFSET 
    
    def random_key(self, key_length: int) -> str:
        """Create a random cryptographic key."""
        return ''.join(chr(randbelow(self.ALPHABET_LENGTH) + self.ORD_OFFSET) for _ in range (key_length))