from secrets import randbelow
from itertools import cycle
from typing import Optional, Generator
from enum import IntEnum


class Direction(IntEnum):
    ENCODE = 1
    DECODE = -1


class Cipher:
    """Encode or decode using a substitution cipher."""
    ALPHABET_LENGTH = 26

    def __init__(self, key: Optional[str] = None) -> None:
        self.key = key or self.random_key(key_length = 100)
        
    def translate(self, text: str, direction: int) -> str:
        """Encode a plaintext string."""
        return ''.join(chr(((direction * key + letter) % self.ALPHABET_LENGTH) + ord('a'))
                       for letter, key in zip(self.ordify(text), cycle(self.ordify(self.key))))
    
    def encode(self, text: str) -> str:
        """Decode an encoded string."""
        return self.translate(text, Direction.ENCODE)

    def decode(self, text: str) -> str:
        """Decode an encoded string."""
        return self.translate(text, Direction.DECODE)

    @staticmethod
    def ordify(text: str) -> Generator[int, None, None]:
        """Represent a string as an int offset from a = 0."""
        return (ord(letter) - ord('a') for letter in text)
    
    @classmethod
    def random_key(cls, key_length: int) -> str:
        """Create a random cryptographic key."""
        return ''.join(chr(randbelow(cls.ALPHABET_LENGTH) + ord('a')) for _ in range (key_length))