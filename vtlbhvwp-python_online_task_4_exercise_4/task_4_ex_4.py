"""
Implement a function `split_by_index(string: str, indexes: List[int]) -> List[str]`
which splits the `string` by indexes specified in `indexes`. 
Only positive index, larger than previous in list is considered valid.
Invalid indexes must be ignored.

Examples:
```python
>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 8, -4, 0, "u", 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>>> split_by_index("no luck", [42])
["no luck"]
```
"""


def is_valid(idx):
    try:
        int(idx)
        assert int(idx) > 0
    except (AssertionError, ValueError):
        return False
    else:
        return True


def split_by_index(string, indexes):
    prev = 0
    result = []
    indexes.insert(0, prev)
    indexes.append(n := len(string))

    for i in range(1, n):
        if is_valid(indexes[i]) and int(indexes[i]) > int(prev):
            result.append(string[int(prev):int(indexes[i])])
            prev = indexes[i]

    return result
