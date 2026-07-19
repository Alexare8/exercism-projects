class Node:
    def __init__(self, value, next = None):
        self._value = value
        self._next = next

    def __iter__(self):
        yield self._value
        if self._next:
            yield from self._next

    def __reversed__(self):
        if self._next:
            yield from reversed(self._next)
        yield self._value

    def value(self):
        return self._value
    
    def next(self):
        return self._next


class LinkedList:
    def __init__(self, values=[]):
        self.head_node = None
        for value in values:
            self.push(value)

    def __len__(self):
        return sum(1 for _ in self)
    
    def __iter__(self):
        if self.head_node:
            yield from self.head_node

    def __reversed__(self):
        if self.head_node:
            yield from reversed(self.head_node)

    def head(self):
        if self.head_node is None:
            raise EmptyListException("The list is empty.")
        return self.head_node

    def push(self, value):
        self.head_node = Node(value, self.head_node)

    def pop(self):
        if self.head_node is None:
            raise EmptyListException("The list is empty.")
        poppednode = self.head_node
        self.head_node = self.head_node._next
        return poppednode._value
    
    def reversed(self):
        return reversed(self)
        

class EmptyListException(Exception):
    pass