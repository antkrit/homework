"""
For a positive integer n calculate the result value, which is equal to the sum
of the odd numbers of n.

Example,
n = 1234 result = 4
n = 246 result = 0

Write it as function.

Note:
Raise TypeError in case of wrong data type or negative integer;
Use of 'functools' module is prohibited, you just need simple for loop.
"""


def sum_odd_numbers(n: int) -> int:
    try:
        x = int(n)
        assert x > 0
        sum_ = 0

        for ch in str(n):
            if (x := int(ch)) % 2:
                sum_ += x

        return sum_
    except (AssertionError, ValueError):
        raise TypeError

print(sum_odd_numbers(246))