from linked_list import Node


class Animal:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.name)

    __str__ = __repr__


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class AnimalShelter:
    '''
    >>> q = AnimalShelter()
    >>> q.dequeue_any()
    >>> q.dequeue_dog()
    >>> q.dequeue_cat()
    >>> q.enqueue(Cat(1))
    >>> q.enqueue(Dog(2))
    >>> q.enqueue(Dog(3))
    >>> q.head
    <Cat: 1> -> <Dog: 2> -> <Dog: 3>
    >>> q.dequeue_any()
    <Cat: 1>
    >>> q.enqueue(Dog(4))
    >>> q.enqueue(Cat(5))
    >>> q.enqueue(Cat(6))
    >>> q.enqueue(Dog(7))
    >>> q.head
    <Dog: 2> -> <Dog: 3> -> <Dog: 4> -> <Cat: 5> -> <Cat: 6> -> <Dog: 7>
    >>> q.dequeue_cat()
    <Cat: 5>
    >>> q.head
    <Dog: 2> -> <Dog: 3> -> <Dog: 4> -> <Cat: 6> -> <Dog: 7>
    >>> q.dequeue_dog()
    <Dog: 2>
    >>> q.head
    <Dog: 3> -> <Dog: 4> -> <Cat: 6> -> <Dog: 7>
    >>> q.dequeue_any()
    <Dog: 3>
    >>> q.dequeue_cat()
    <Cat: 6>
    >>> q.enqueue(Cat(8))
    >>> q.dequeue_any()
    <Dog: 4>
    >>> q.dequeue_cat()
    <Cat: 8>
    >>> q.enqueue(Cat(9))
    >>> q.dequeue_cat()
    <Cat: 9>
    '''
    def __init__(self):
        self.head = None
        self.last = None

    def enqueue(self, animal):
        node = Node(animal)
        if not self.head:
            self.head = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    def dequeue_any(self):
        if not self.head:
            return None

        value = self.head.value
        if self.head == self.last:
            self.last = None
        self.head = self.head.next
        return value

    def _dequeue(self, animal):
        prev = None
        curr = self.head
        while curr:
            if isinstance(curr.value, animal):
                if prev and curr.next:
                    prev.next = curr.next
                elif curr == self.head:
                    self.head = curr.next
                if self.last == curr:
                    self.last = prev
                return curr.value
            else:
                prev = curr
                curr = curr.next
        return None

    def dequeue_dog(self):
        return self._dequeue(Dog)

    def dequeue_cat(self):
        return self._dequeue(Cat)


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)

