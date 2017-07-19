import random


# knuth!
def shuffle(xs):
    '''
    >>> xs = [1, 2, 3, 4, 5, 6]
    >>> shuffle(xs)
    >>> set(xs).difference(range(1, 7))
    set()
    '''
    for i in range(1, len(xs)):
        r = random.randint(0, i)
        xs[i], xs[r] = xs[r], xs[i]


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
