"""
Implement a bunch of functions which receive a changeable number of strings and return next
parameters:
1) characters that appear in all strings
2) characters that appear in at least one string
3) characters that appear at least in two strings
  Note: raise ValueError if there are less than two strings
4) characters of alphabet, that were not used in any string
  Note: use `string.ascii_lowercase` for list of alphabet letters

Note: raise TypeError in case of wrong data type

Examples,
```python
test_strings = ["hello", "world", "python", ]
print(chars_in_all(*test_strings))
>>> {'o'}
print(chars_in_one(*test_strings))
>>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
print(chars_in_two(*test_strings))
>>> {'h', 'l', 'o'}
print(not_used_chars(*test_strings))
>>> {'q', 'k', 'g', 'f', 'j', 'u', 'a', 'c', 'x', 'm', 'v', 's', 'b', 'z', 'i'}
"""
import string
from itertools import combinations


def chars_in_all(*strings):
    try:
        result = chars_in_one(*strings)
        for seq in strings:
            if isinstance(seq, list):
                for str_ in seq:
                    result = result & set(str_)
            else:
                result = result & set(seq)

        return result
    except Exception:
        raise TypeError


def chars_in_one(*strings):
    return set(''.join(strings))


def chars_in_two(*strings):
    if len(strings) < 2:
        raise ValueError

    comb = list(combinations(strings, 2))
    result = set(comb[0][0]) & set(comb[0][1])
    for c in comb:
        result = result | (set(c[0]) & set(c[1]))

    return result


def not_used_chars(*strings):
    ascii = string.ascii_lowercase
    return set([ch for ch in ascii]) ^ chars_in_one(*strings)
