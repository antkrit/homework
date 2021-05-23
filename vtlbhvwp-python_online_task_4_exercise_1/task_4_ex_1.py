"""04 Task 1.1
Implement a function which receives a string and replaces all " symbols with ' and vise versa. The
function should return modified string.
Usage of any replacing string functions is prohibited.
"""
MAP_DICT = {
    '\'': '\"',
    '\"': '\''
}


def swap_quotes(string: str) -> str:
    result = ''
    for ch in string:
        result += MAP_DICT[ch] if ch in MAP_DICT else ch

    return result
