def compress(s):
    '''
    >>> compress('aabcccccaaa') == 'a2b1c5a3'
    True
    >>> compress('aabb') == 'aabb'
    True
    '''
    if len(s) <= 2:
        return s

    acc = []
    k = s[0]
    v = 1

    for i, c in enumerate(s[1:]):
        if k != c:
            acc.append(k + str(v))
            k = c
            v = 1
        else:
            v += 1
    acc.append(k + str(v))
    z = ''.join(acc)

    if len(z) == len(s):
        return s
    return z


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
