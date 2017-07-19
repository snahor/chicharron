def check_permutation0(s0, s1):
    '''
    O(nlgn)
    >>> check_permutation0('foo', 'ofo')
    True
    '''
    if len(s0) != len(s1):
        return False
    return sorted(s0) == sorted(s1)


def check_permutation1(s0, s1):
    '''
    O(n)
    O(n) extra space
    >>> check_permutation1('foo', 'ofo')
    True
    '''
    if len(s0) != len(s1):
        return False
    d = {}
    for c in s0:
        d[c] = d.get(c, 0) + 1
    for c in s1:
        if not c in d:
            return False
        d[c] -= 1
        if d[c] < 0:
            return False
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
