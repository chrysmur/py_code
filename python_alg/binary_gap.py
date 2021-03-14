#!/usr/bin/python3
'''
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.
For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
'''

def solution(N):
    # check for not integers
    if type(N) != int:
        return "Enter an integer"

    # convert to a binary string
    n_bin = "{0:b}".format(N)
    max_gap = 0
    gap = 0
    for i in range(len(n_bin)):
        if n_bin[i] == '0':
            gap += 1
            continue
        max_gap = max(max_gap, gap)
        gap = 0
    return max_gap


# TEST
assert solution(32) == 0
assert solution(561892) == 3
assert solution(1041) == 5
assert solution(51712) == 2
assert solution(1376796946) == 5