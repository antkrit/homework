"""
Implement function count_letters, which takes string as an argument and
returns a dictionary that contains letters of given string as keys and a
number of their occurrence as values.

Example:
print(count_letters("Hello world!"))
Result: {'H': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

Note: Pay attention to punctuation.
"""
import re


def count_letters(s: str):
    lttrs = re.sub('[^a-zA-Z]', '', s)
    result = dict()

    for ch in lttrs:
        result[ch] = result.get(ch, 0) + 1

    return result
