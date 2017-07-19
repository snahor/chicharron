def is_substring(s0, s1):
    return s1 in s0


def is_rotation(s0, s1):
    '''
    >>> is_rotation('abcd', 'cdab')
    True
    '''
    if len(s0) != len(s1):
        return False
    # abcd cdab
    # cdabcdab

    return is_substring(s1 + s1, s0)


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
