from linked_list import Node


def reverse(head):
    '''
    >>> head = Node(1)
    >>> reverse(head)
    1
    >>> head = Node(1, Node(2, Node(3)))
    >>> reverse(head)
    3 -> 2 -> 1
    >>> reverse(reverse(head))
    1 -> 2 -> 3
    '''
    new_head = None
    curr = head
    while curr:
        new_head = Node(curr.value, new_head)
        curr = curr.next
    return new_head



def is_palindrome(head):
    '''
    >>> is_palindrome(Node(1))
    True
    >>> is_palindrome(Node(1, Node(2, Node(3))))
    False
    >>> is_palindrome(Node(1, Node(2, Node(3, Node(2, Node(1))))))
    True
    '''
    new_head = reverse(head)
    while head:
        if head.value != new_head.value:
            return False
        head = head.next
        new_head = new_head.next
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
