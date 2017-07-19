from linked_list import Node


def sum_linked_lists(a, b):
    '''
    >>> a = Node(7, Node(1, Node(6)))
    >>> b = Node(5, Node(9, Node(2)))
    >>> sum_linked_lists(a, b)
    2 -> 1 -> 9
    '''
    c = None
    out = None
    carrier = 0
    while a and b:
        s = a.value + b.value
        node = Node((s % 10) + carrier)
        carrier = s // 10
        if c is None:
            out = node
        else:
            c.next = node
        c = node
        a = a.next
        b = b.next

    while a:
        c.next = Node(a.value)
        a = a.next
    while b:
        c.next = Node(b.value)
        b = b.next
    return out


if __name__ == '__main__':
    import doctest
    doctest.testmod()

