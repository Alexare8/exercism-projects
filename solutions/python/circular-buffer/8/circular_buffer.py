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
        return self.oldest is not None and self.newest == (self.oldest - 1) % self.capacity

    @property
    def empty(self) -> bool:
        return self.oldest is None
    
    def read(self):
        print(f"Newest {self.newest}, Oldest {self.oldest}, Pre-Read buffer {self.buffer}")
        if self.empty:
            raise BufferEmptyException("Circular buffer is empty")
        out = self.buffer[self.oldest]
        self.buffer[self.oldest] = None
        self.oldest = (self.oldest + 1) % self.capacity
        if self.oldest == (self.newest + 1) % self.capacity:
            self.clear()
        print(f"Newest {self.newest}, Oldest {self.oldest}, Post-Read buffer {self.buffer}")
        return out

    def write(self, data) -> None:
        print(f"Newest {self.newest}, Oldest {self.oldest}, Pre-Write buffer {self.buffer}")
        if self.full:
            raise BufferFullException("Circular buffer is full")
        if self.empty:
            self.newest = 0
            self.oldest = self.newest
            self.buffer[self.newest] = data
            return            
        self.newest = (self.newest + 1) % self.capacity
        self.buffer[self.newest] = data
        
        print(f"Newest {self.newest}, Oldest {self.oldest}, Post-Write buffer {self.buffer}")

    def overwrite(self, data) -> None:
        if not self.full:
            self.write(data)
            return
        
        print(f"Newest {self.newest}, Oldest {self.oldest}, Pre-Overwrite buffer {self.buffer}")
        self.buffer[self.oldest] = data
        self.newest = self.oldest
        self.oldest = (self.oldest + 1) % self.capacity
        print(f"Newest {self.newest}, Oldest {self.oldest}, Post-Overwrite buffer {self.buffer}")

    def clear(self) -> None:
        self.buffer = [None for _ in range(self.capacity)]
        self.oldest = None
        self.newest = None
