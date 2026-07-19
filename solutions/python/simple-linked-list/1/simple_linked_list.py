class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

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
        node = self.head_node
        count = 0
        while not node is None:
            count += 1
            node = node._next
        return count
    
    def __iter__(self):
        while len(self):
            yield self.pop()

    def head(self):
        if self.head_node is None:
            raise EmptyListException("The list is empty.")
        return self.head_node

    def push(self, value):
        newnode = Node(value)
        newnode._next = self.head_node
        self.head_node = newnode

    def pop(self):
        if self.head_node is None:
            raise EmptyListException("The list is empty.")
        poppednode = self.head_node
        self.head_node = self.head_node._next
        return poppednode._value

    def reversed(self):
        for value in list(self)[::-1]:
            yield value


class EmptyListException(Exception):
    pass