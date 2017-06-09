# Write a program which implements a stack interface for integers. The
# interface should have ‘push’ and ‘pop’ functions. Your task is to ‘push’ a
# series of integers and then ‘pop’ and print every alternate integer.
#
# INPUT SAMPLE:
#
# Your program should accept a file as its first argument. The file contains a
# series of space delimited integers, one per line.
#
# For example:
# 1 2 3 4
# 10 -2 3 4
#
# OUTPUT SAMPLE:
#
# Print to stdout every alternate space delimited integer, one per line.
#
# For example:
# 4 2
# 4 -2

import sys


class DerpStack(list):
    push = list.append

    def pop(self):
        x = super().pop()
        super().pop()
        return x


with open(sys.argv[1], 'r') as f:
    for line in f:
        s = DerpStack()
        for i in line.split():
            s.push(i)
        while s:
            print(s.pop(), end=' ')
        print()
