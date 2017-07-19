from linked_list import Node


def delete_node(node):
    '''
    >>> node = Node('c', Node('d', Node('e')))
    >>> linked_list = Node('a', Node('b', node))
    >>> linked_list
    a -> b -> c -> d -> e
    >>> delete_node(node)
    >>> linked_list
    a -> b -> d -> e
    >>> node
    d -> e
    >>> delete_node(node)
    >>> linked_list
    a -> b -> e
    '''
    if not node.next:
        return
    node.value = node.next.value
    node.next = node.next.next



if __name__ == '__main__':
    import doctest
    doctest.testmod()

