class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full."""


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty."""


class CircularBuffer:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity + 1
        self.clear()

    @property
    def full(self) -> bool:
        return self.oldest == self.mod_inc(self.next)

    @property
    def empty(self) -> bool:
        return self.oldest == self.next
    
    def read(self):
        if self.empty:
            raise BufferEmptyException("Circular buffer is empty")
        out = self.buffer[self.oldest]
        self.oldest = self.mod_inc(self.oldest)
        return out

    def write(self, data) -> None:
        if self.full:
            raise BufferFullException("Circular buffer is full")
        self.buffer[self.next] = data          
        self.next = self.mod_inc(self.next)

    def overwrite(self, data) -> None:
        if self.full:
            self.read()   #Bump oldest forward before overwriting
        self.write(data)        

    def clear(self) -> None:
        self.buffer = [None for _ in range(self.capacity)]
        self.oldest = 0
        self.next = 0

    def mod_inc(self, num: int) -> int:
        """Increment with modulus wrapping."""
        return (num + 1) % self.capacity
