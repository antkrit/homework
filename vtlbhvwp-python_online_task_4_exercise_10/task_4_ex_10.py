"""
Create a function sum_binary_1 that for a positive integer n
calculates the result value, which is equal to the sum of the
“1” in the binary representation of n otherwise, returns None.

Example,
n = 14 = 1110 result = 3
n = 128 = 10000000 result = 1
"""


def sum_binary_1(n: int):
    try:
        assert isinstance(n, int)
        assert n > 0

        bnumber = bin(int(n))[2:]

        return sum(list(map(int, str(bnumber))))
    except AssertionError:
        return None
