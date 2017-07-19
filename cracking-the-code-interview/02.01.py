from linked_list import Node


def remove_duplicates(node):
    '''
    O(n) O(n) extra space
    >>> list = Node(1, Node(1))
    >>> remove_duplicates(list)
    >>> list
    1
    >>> list = Node(1, Node(1, Node(1)))
    >>> remove_duplicates(list)
    >>> list
    1
    >>> list = Node(1, Node(2, Node(3)))
    >>> remove_duplicates(list)
    >>> list
    1 -> 2 -> 3
    '''
    visited = set()
    prev = None
    while node:
        if node.value not in visited:
            visited.add(node.value)
            prev = node
            node = node.next
        else:
            prev.next = node.next
            if node.next:
                node = node.next
            else:
                break


def remove_duplicates1(node):
    '''
    O(n^2) no extra space
    >>> list = Node(1, Node(1))
    >>> remove_duplicates1(list)
    >>> list
    1
    >>> list = Node(1, Node(1, Node(1)))
    >>> remove_duplicates1(list)
    >>> list
    1
    >>> list = Node(1, Node(2, Node(3)))
    >>> remove_duplicates1(list)
    >>> list
    1 -> 2 -> 3
    '''
    while node and node.next:
        curr = node
        while curr.next:
            if node.value == curr.next.value:
                curr.next = curr.next.next
            else:
                curr = curr.next
        node = node.next


if __name__ == '__main__':
    import doctest
    doctest.testmod()
