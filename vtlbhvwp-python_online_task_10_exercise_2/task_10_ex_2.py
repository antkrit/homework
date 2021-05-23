"""Implement a function `most_common_words(file_path: str, top_words: int) -> list`
which returns most common words in the file.
<file_path> - system path to the text file
<top_words> - number of most common words to be returned

Example:

print(most_common_words(file_path, 3))
>>> ['donec', 'etiam', 'aliquam']
> NOTE: Remember about dots, commas, capital letters etc.
"""
import re


def most_common_words(text, top_words):
    result = {}
    with open(text, 'r') as f:
        words = f.read().split()
        for w in words:
            key_ = re.sub('[^a-z]', '', w.lower())
            result[key_] = result.get(key_, 0) + 1

    sorted_words = sorted(result, key=result.get, reverse=True)
    return sorted_words[:top_words]
