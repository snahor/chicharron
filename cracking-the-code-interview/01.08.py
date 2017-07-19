def zero_matrix(matrix, m, n):
    '''
    >>> matrix = [[1,0,3],[4,5,6],[7,8,9]]
    >>> zero_matrix(matrix, 3, 3)
    >>> matrix
    [[0, 0, 0], [4, 0, 6], [7, 0, 9]]
    '''
    # 1 0 3  0 0 0
    # 1 2 3  1 0 3
    # 1 2 3  1 0 3

    rows = set()
    cols = set()

    for i in range(m):
        for j in range(n):
            if j in cols:
                continue
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for row in rows:
        for j in range(n):
            matrix[row][j] = 0

    for col in cols:
        for i in range(m):
            matrix[i][col] = 0


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
