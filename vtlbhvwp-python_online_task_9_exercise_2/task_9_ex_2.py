"""
Write a function that checks whether a string is a palindrome or not.
Return 'True' if it is a palindrome, else 'False'.

Note:
Usage of reversing functions is required.
Raise ValueError in case of wrong data type

To check your implementation you can use strings from here
(https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).
"""
import re

def is_palindrome(test_string: str) -> bool:
    if not isinstance(test_string, str):
        raise ValueError

    test_string = re.sub('[^a-z]', '', test_string.lower())
    if test_string == ''.join(reversed(test_string)):
        return True
    return False
