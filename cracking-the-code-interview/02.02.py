from linked_list import Node


def kth_to_last(k, head):
    '''
    >>> kth_to_last(1, Node(1, Node(2, Node(3, Node(4, Node(5))))))
    5

    >>> kth_to_last(4, Node(1, Node(2, Node(3, Node(4, Node(5))))))
    2 -> 3 -> 4 -> 5

    >>> kth_to_last(7, Node(1, Node(2, Node(3, Node(4, Node(5))))))
    '''
    n = 1
    curr = head

    while curr:
        n += 1
        curr = curr.next

    if k > n:
        return None

    m = n - k
    curr = head
    while m > 1:
        curr = curr.next
        m -= 1

    return curr


if __name__ == '__main__':
    import doctest
    doctest.testmod()
