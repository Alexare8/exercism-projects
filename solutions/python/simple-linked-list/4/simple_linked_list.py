from __future__ import annotations
from typing import Generator, Optional, TypeVar

data = TypeVar("data")


class Node:
    """Store a value and a pointer for a LinkedList."""
    def __init__(self, value: data, next: Optional[Node]) -> None:
        self._value = value
        self._next = next

    def __iter__(self) -> Generator[data, None, None]:
        yield self._value
        if self._next:
            yield from self._next

    def __reversed__(self) -> Generator[data, None, None]:
        if self._next:
            yield from reversed(self._next)
        yield self._value

    def value(self) -> data:
        """Return the value stored in the node."""
        return self._value
    
    def next(self) -> Node|None:
        """Return the next node in the LinkedList."""
        return self._next


class LinkedList:
    """Store data in a singly-linked list."""
    def __init__(self, values: list[data] = []) -> None:
        self.head_node: Node|None = None
        for value in values:
            self.push(value)

    def __len__(self) -> int:
        return sum(1 for _ in self)
    
    def __iter__(self) -> Generator[Node, None, None]:
        if self.head_node:
            yield from self.head_node

    def __reversed__(self) -> Generator[Node, None, None]:
        if self.head_node:
            yield from reversed(self.head_node)

    def head(self) -> Node:
        """Return the head node of the list."""
        if self.head_node is None:
            raise EmptyListException("The list is empty.")
        return self.head_node

    def push(self, value: data) -> None:
        """Create a new node at the head of the list."""
        self.head_node = Node(value, self.head_node)

    def pop(self) -> data:
        """Remove the head node of the list and return it's value."""
        if self.head_node is None:
            raise EmptyListException("The list is empty.")
        poppednode = self.head_node
        self.head_node = self.head_node._next
        return poppednode._value
    
    def reversed(self) -> reversed[Node]:
        """Return the list in reverse order."""
        return reversed(self)
        

class EmptyListException(Exception):
    pass