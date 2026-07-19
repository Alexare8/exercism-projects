class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message: str) -> None:
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message: str) -> None:
        self.message = message


class CircularBuffer:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.clear()

    @property
    def full(self) -> bool:
        return self.oldest == self._next and self.buffer[0] != []

    @property
    def empty(self) -> bool:
        return self.oldest == self._next and self.buffer[0] == []
    
    def read(self):
        if self.empty:
            raise BufferEmptyException("Circular buffer is empty")
        out = self.buffer[self.oldest]
        self.buffer[self.oldest] = []
        self.oldest = (self.oldest + 1) % self.capacity
        return out

    def write(self, data) -> None:
        if self.full:
            raise BufferFullException("Circular buffer is full")
        self.buffer[self._next] = data
        self._next = (self._next + 1) % self.capacity

    def overwrite(self, data) -> None:
        if not self.full:
            self.write(data)
            return
        
        self.buffer[self.oldest] = data
        self.oldest = (self.oldest + 1) % self.capacity
        self._next = self.oldest

    def clear(self) -> None:
        self.buffer = [[] for _ in range(self.capacity)]
        self.oldest = 0
        self._next = 0
