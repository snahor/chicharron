from stack import Stack


class Queue:
    '''
    >>> q = Queue()
    >>> q.dequeue()
    >>> q.enqueue(1)
    >>> q.enqueue(2)
    >>> q.enqueue(3)
    >>> q.dequeue()
    1
    >>> q.dequeue()
    2
    >>> q.enqueue(4)
    >>> q.dequeue()
    3
    '''
    def __init__(self):
        self.s0 = Stack()
        self.s1 = Stack()

    def enqueue(self, value):
        self.s0.push(value)

    def peek(self):
        pass

    def is_empty(self):
        pass

    def dequeue(self):
        if self.s1.is_empty():
            while not self.s0.is_empty():
                self.s1.push(self.s0.pop())
        return self.s1.pop()


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
