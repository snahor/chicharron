from linked_list import Node


class Stack:
    '''
    >>> s = Stack()
    >>> s.push(1)
    >>> s.push(2)
    >>> s.peek()
    2
    >>> s.pop()
    2
    >>> s.pop()
    1
    >>> s.pop()
    >>> s.is_empty()
    True
    '''
    def __init__(self):
        self.node = None

    def push(self, value):
        self.node = Node(value, self.node)

    def pop(self):
        if self.node:
            node = self.node
            self.node = node.next
            return node.value
        return None

    def peek(self):
        return self.node.value if self.node else None

    def is_empty(self):
        return self.node is None


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
