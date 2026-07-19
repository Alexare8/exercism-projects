class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full."""
    #def __init__(self, message: str) -> None:
    #    self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty."""
    def __init__(self, message: str) -> None:
        self.message = message


class CircularBuffer:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity + 1
        self.clear()

    @property
    def full(self) -> bool:
        return self.oldest == self.mod_inc(self._next)

    @property
    def empty(self) -> bool:
        return self.oldest == self._next
    
    def read(self):
        if self.empty:
            raise BufferEmptyException("Circular buffer is empty")
        out = self.buffer[self.oldest]
        self.oldest = self.mod_inc(self.oldest)
        return out

    def write(self, data) -> None:
        if self.full:
            raise BufferFullException("Circular buffer is full")
        self.buffer[self._next] = data          
        self._next = self.mod_inc(self._next)

    def overwrite(self, data) -> None:
        if self.full:
            self.oldest = self.mod_inc(self.oldest)
        self.write(data)        

    def clear(self) -> None:
        self.buffer = [None for _ in range(self.capacity)]
        self.oldest = 0
        self._next = 0

    def mod_inc(self, num: int) -> int:
        """Increment with modulus wrapping."""
        return (num + 1) % self.capacity
