from linked_list import Node


def loop_detection(node):
    '''
    >>> e = Node('e')
    >>> d = Node('d', e)
    >>> c = Node('c', d)
    >>> head = Node('a', Node('b', c))
    >>> head
    a -> b -> c -> d -> e
    >>> e.next = c
    >>> head
    a -> b -> c -> d -> e -> c -> d ...
    >>> loop_detection(head)
    c -> ...
    >>> loop_detection(Node(1, Node(2)))
    '''
    visited = set()
    while node:
        if id(node) not in visited:
            visited.add(id(node))
            node = node.next
        else:
            return node
    return None


def loop_detection1(node):
    '''
    >>> e = Node('e')
    >>> d = Node('d', e)
    >>> c = Node('c', d)
    >>> head = Node('a', Node('b', c))
    >>> e.next = c
    >>> loop_detection1(head)
    c -> ...
    >>> loop_detection1(Node(1, Node(2)))
    '''
    fast = node
    slow = node

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            break

    if not fast or not fast.next:
        return None

    slow = node
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return fast


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
