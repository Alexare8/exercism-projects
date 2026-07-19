from secrets import randbelow
from itertools import cycle


class Cipher:
    """Encode or decode using a substitution cipher."""
    ORD_A = ord('a')
    ENCODE = 1
    DECODE = -1

    def __init__(self, key: str | None = None) -> None:
        if key is None:
            key = self.random_key()
        self.key = key
        
    def encode(self, text: str, direction: int = ENCODE) -> str:
        """Encode a plaintext string."""
        return ''.join(chr(((direction * key + letter) % 26) + self.ORD_A) for letter, key in zip(self.ordify(text), cycle(self.ordify(self.key))))

    def decode(self, text: str) -> str:
        """Decode an encoded string."""
        return self.encode(text, self.DECODE)

    def ordify(self, text: str) -> list[int]:
        """Represent a string as an int offset from a = 0."""
        return [ord(letter) - self.ORD_A for letter in text]
    
    def random_key(self) -> str:
        """Create a random cryptographic key."""
        return ''.join(chr(randbelow(26) + self.ORD_A) for _ in range (100))