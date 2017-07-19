from stack import Stack


def sort_stack(stack):
    '''
    >>> s = Stack()
    >>> s.push(3)
    >>> s.push(1)
    >>> s.push(2)
    >>> sort_stack(s)
    >>> s.is_empty()
    False
    >>> s.pop()
    1
    >>> s.pop()
    2
    >>> s.pop()
    3
    >>> s.pop()
    '''
    # s.push(4); s.push(2); s.push(3); s.push(1); s.push(5); s.push(0)
    tmp = Stack()
    while not stack.is_empty():
        value = stack.pop()
        while not tmp.is_empty() and tmp.peek() > value:
            stack.push(tmp.pop())
        tmp.push(value)

    while not tmp.is_empty():
        stack.push(tmp.pop())


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)

