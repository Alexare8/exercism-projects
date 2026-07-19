class Node:
    def __init__(self, value, next = None):
        self._value = value
        self._next = next

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
        node = self.head_node
        while not node is None:
            yield node._value
            node = node._next

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
        yield from reversed(list(self))


class EmptyListException(Exception):
    pass