def is_unique0(s):
    '''
    O(n)
    O(n) extra space
    >>> is_unique0('qwertyuiop')
    True
    >>> is_unique0('foo')
    False
    '''
    if not s:
        return False
    return len(s) == len(set(s))


def is_unique1(s):
    '''
    O(nlgn)
    no extra space
    >>> is_unique1('qwertyuiop')
    True
    >>> is_unique1('foo')
    False
    '''
    if not s:
        return False
    if len(s) == 1:
        return True
    cs = sorted(s)
    for i in range(1, len(s)):
        if cs[i - 1] == cs[i]:
            return False
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
