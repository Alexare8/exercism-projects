from secrets import randbelow
from itertools import cycle
from typing import Optional, Generator
from enum import Enum


class Direction(Enum):
    ENCODE = 1
    DECODE = -1


class Cipher:
    """Encode or decode using a substitution cipher."""
    ALPHABET_LENGTH = 26

    def __init__(self, key: Optional[str] = None) -> None:
        self.key = key or self.random_key(key_length = 100)
        
    def translate(self, text: str, direction: Direction) -> str:
        """Encode a plaintext string."""
        return ''.join(chr(((direction.value * key + letter) % self.ALPHABET_LENGTH) + ord('a'))
                       for letter, key in zip(self.ordify(text), cycle(self.ordify(self.key))))
    
    def encode(self, text: str) -> str:
        """Decode an encoded string."""
        return self.translate(text, Direction.ENCODE)

    def decode(self, text: str) -> str:
        """Decode an encoded string."""
        return self.translate(text, Direction.DECODE)

    @classmethod
    def ordify(cls, text: str) -> Generator[int, None, None]:
        """Represent a string as an int offset from a = 0."""
        for letter in text:
            yield ord(letter) - ord('a') 
    
    @classmethod
    def random_key(cls, key_length: int) -> str:
        """Create a random cryptographic key."""
        return ''.join(chr(randbelow(cls.ALPHABET_LENGTH) + ord('a')) for _ in range (key_length))