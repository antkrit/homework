"""
Task04_1_2
Write `is_palindrome` function that checks whether a string is a palindrome or not
Returns 'True' if it is palindrome, else 'False'

To check your implementation you can use strings from here
(https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).

Note:
Usage of any reversing functions is prohibited.
The function has to ignore special characters, whitespaces and different cases
Raise ValueError in case of wrong data type
"""
from re import sub


def is_palindrome(test_string: str) -> bool:
    
    try:
        assert isinstance(test_string, str)

        test_string = sub('[^A-Za-z]', '', test_string).lower()
        for i, ch in enumerate(test_string):
            if ch != test_string[-i - 1]:
                return False

        return True
    except AssertionError:
        raise ValueError
