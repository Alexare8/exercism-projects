class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full."""
    def __init__(self, message: str) -> None:
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty."""
    def __init__(self, message: str) -> None:
        self.message = message


class CircularBuffer:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.clear()

    @property
    def full(self) -> bool:
        return self.oldest is not None and self.oldest == self.mod_inc(self.newest)

    @property
    def empty(self) -> bool:
        return self.oldest is None
    
    def read(self):
        if self.empty:
            raise BufferEmptyException("Circular buffer is empty")
        out = self.buffer[self.oldest]
        self.buffer[self.oldest] = None
        self.oldest = self.mod_inc(self.oldest)
        if self.oldest == self.mod_inc(self.newest):
            self.clear()
        return out

    def write(self, data) -> None:
        if self.full:
            raise BufferFullException("Circular buffer is full")
        if self.empty:
            self.newest = 0
            self.oldest = self.newest
            self.buffer[self.newest] = data
            return            
        self.newest = self.mod_inc(self.newest)
        self.buffer[self.newest] = data

    def overwrite(self, data) -> None:
        if not self.full:
            self.write(data)
            return
        
        self.buffer[self.oldest] = data
        self.newest = self.oldest
        self.oldest = self.mod_inc(self.oldest)

    def clear(self) -> None:
        self.buffer = [None for _ in range(self.capacity + 1)]
        self.oldest = None
        self.newest = None

    def mod_inc(self, num: int) -> int:
        """Increment with modulus wrapping."""
        return (num + 1) % self.capacity
