from linked_list import Node

def length(node):
    n = 0
    while node:
        n += 1
        node = node.next
    return n


def intersection(nodex, nodey):
    '''
    >>> node = Node(1, Node(2))
    >>> nodex = Node(1, Node(2, Node(1, Node(2, node))))
    >>> nodey = Node(4, Node(3, node))
    >>> intersection(nodex, nodey)
    1 -> 2
    >>> intersection(Node(1, Node(2)), node)
    '''
    lenx = length(nodex)
    leny = length(nodey)

    if lenx < leny:
        nodey, nodex = nodex, nodey

    while lenx > leny:
        nodex = nodex.next
        lenx -= 1

    while nodex and nodey:
        if nodex == nodey:
            return nodex
        nodex = nodex.next
        nodey = nodey.next

    return None


if __name__ == '__main__':
    import doctest
    doctest.testmod()
