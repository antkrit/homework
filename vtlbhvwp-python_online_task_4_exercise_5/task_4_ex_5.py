"""Implement a function `get_digits(args: int) -> Tuple[int]` which receives 
arbitrary amount of arguments and returns a tuple of digits of given integers.

Example:
```python
>>> get_digits(8717, 82911, 99)
(8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
```
"""


def get_digits(*args):
    result = []

    for num in args:
        digits = [int(x) for x in str(num)]
        result.extend(digits)

    return tuple(result)