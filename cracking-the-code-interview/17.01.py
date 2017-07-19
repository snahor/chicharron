def add_without_plus(a, b):
    '''
    >>> add_without_plus(12, 31)
    43
    >>> add_without_plus(0, 1)
    1
    >>> add_without_plus(19, 23)
    42
    '''
    if not b:
        return a
    sum = a ^ b
    carry = (a & b) << 1

    return add_without_plus(sum, carry)


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
