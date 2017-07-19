def urlify0(bs, true_length):
    '''
    >>> given = 'foo bar baz      '
    >>> expected = 'foo%20bar%20baz  '
    >>> length = 11
    >>> input = bytearray(given.encode())
    >>> output = bytearray(expected.encode())
    >>> urlify0(input, length)
    >>> input == output
    True
    '''
    space = ord(' ')

    # count spaces
    spaces = sum(1 for i in range(true_length) if bs[i] == space)

    # actual string length
    total_length = true_length + spaces * 2

    index = total_length - 1
    cs = bytearray(b'%20')

    for i in range(true_length - 1, -1, -1):
        if bs[i] == space:
            bs[index-2], bs[index-1], bs[index] = cs
            index -= 3
        else:
            bs[index] = bs[i]
            index -= 1


def urlify1(s: str, true_length: int) -> str:
    '''
    >>> given = 'foo bar baz      '
    >>> expected = 'foo%20bar%20baz  '
    >>> length = 11
    >>> urlify1(given, length)
    'foo%20bar%20baz  '
    '''
    spaces = sum(1 for i in range(true_length) if s[i] == ' ')
    total_length = true_length + spaces * 2
    cs = list(s)
    index = 0
    for i in range(true_length):
        if s[i] == ' ':
            cs[index], cs[index+1], cs[index+2] = '%20'
            index += 3
        else:
            cs[index] = s[i]
            index += 1
    return ''.join(cs)


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
