from stack import Stack


class StackMin(Stack):
    '''
    >>> s = StackMin()
    >>> s.push(4)
    >>> s.min()
    4
    >>> s.push(5)
    >>> s.min()
    4
    >>> s.push(2)
    >>> s.min()
    2
    >>> s.pop()
    >>> s.min()
    4
    '''
    def __init__(self):
        super().__init__()
        self.min_stack = Stack()

    def push(self, value):
        super().push(value)
        if self.min_stack.is_empty() or value < self.min_stack.peek():
            self.min_stack.push(value)

    def pop(self):
        value = super().pop()
        if value == self.min_stack.peek():
            self.min_stack.pop()

    def min(self):
        return self.min_stack.peek()


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
