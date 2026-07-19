from secrets import randbelow
from itertools import cycle
from typing import Optional
from enum import IntEnum
from string import ascii_lowercase


class Direction(IntEnum):
    ENCODE = 1
    DECODE = -1


class Cipher:
    """Encode or decode using a substitution cipher."""
    ALPHABET = ascii_lowercase

    def __init__(self, key: Optional[str] = None) -> None:
        self.key = key or self.random_key(key_length = 100)
        
    def translate(self, text: str, direction: int) -> str:
        """Encode a plaintext string."""
        return ''.join(self.ALPHABET[(direction * self.ALPHABET.index(key) + self.ALPHABET.index(letter)) % len(self.ALPHABET)]
                       for letter, key in zip(text, cycle(self.key)))
    
    def encode(self, text: str) -> str:
        """Decode an encoded string."""
        return self.translate(text, Direction.ENCODE)

    def decode(self, text: str) -> str:
        """Decode an encoded string."""
        return self.translate(text, Direction.DECODE)
    
    @classmethod
    def random_key(cls, key_length: int) -> str:
        """Create a random cryptographic key."""
        return ''.join(cls.ALPHABET[randbelow(len(cls.ALPHABET))] for _ in range (key_length))
    