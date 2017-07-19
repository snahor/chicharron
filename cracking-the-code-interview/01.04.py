def is_palindrome_permutation0(s):
    '''
    >>> is_palindrome_permutation0('Tact Coa')
    True
    '''
    valid_chars = 0
    d = {}
    for c in s:
        if c == ' ':
            continue
        char = c.lower()
        d[char] = d.get(char, 0) + 1
        valid_chars += 1

    evens = 0
    odds = 0
    for _, v in d.items():
        if v % 2 == 0:
            evens += 1
        else:
            odds += 1
    # print(d,evens,odds)
    return evens * 2 == valid_chars or evens * 2 + odds == valid_chars

# aba   aab   a:2 b:1      evens: 1 odds: 1
# abba  aabb  a:2 b:2      evens: 2 odds: 0
# abcba aabbc a:2 b:2 c:1  evens: 2 odds: 1
# acbca aab2c a:2 b:1 c:2  evens: 2 odds: 1

def is_palindrome_permutation1(s):
    '''
    >>> is_palindrome_permutation1('Tact Coa')
    True
    '''
    d = {}
    odds = 0
    for c in s:
        if c == ' ':
            continue
        char = c.lower()
        d[char] = d.get(char, 0) + 1
        if d[char] % 2 == 0:
            odds -= 1
        else:
            odds += 1

    return 0 <= odds <= 1


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
