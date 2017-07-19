from linked_list import Node


class Queue:
    '''
    >>> q = Queue()
    >>> q.enqueue(1)
    >>> q.enqueue(2)
    >>> q.enqueue(3)
    >>> q.dequeue()
    1
    >>> q.dequeue()
    2
    >>> q.enqueue(4)
    >>> q.enqueue(5)
    >>> q.dequeue()
    3
    >>> q.dequeue()
    4
    >>> q.dequeue()
    5
    >>> q.dequeue()
    '''
    def __init__(self):
        self.head = None
        self.last = None

    def enqueue(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    def dequeue(self):
        if not self.head:
            return None
        node = self.head
        self.head = node.next
        if self.last == node:
            self.last = node.next
        return node.value

    def is_empty(self):
        return self.head is None


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
