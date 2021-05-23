"""
Task04_3

Implement a function which works the same as str.split

Note:
Usage of str.split method is prohibited
Raise ValueError in case of wrong data type
"""


def split_alternative(str_to_split: str, delimiter=' ') -> list:
    result = []
    temp = ''

    try:
        assert isinstance(str_to_split, str)

        for ch in str_to_split:
            if ch == delimiter:
                result.append(temp)
                temp = ''
            else:
                temp += ch

        result.append(temp)

        return result
    except AssertionError:
        raise ValueError
