"""
Write a function converting a Roman numeral from a given string N into an Arabic numeral.
Values may range from 1 to 100 and may contain invalid symbols.
Invalid symbols and numerals out of range should raise ValueError.

Numeral / Value:
I: 1
V: 5
X: 10
L: 50
C: 100

Example:
N = 'I'; result = 1
N = 'XIV'; result = 14
N = 'LXIV'; result = 64

Example of how the task should be called:
python3 task_3_ex_2.py LXIV

Note: use `argparse` module to parse passed CLI arguments
"""
import argparse


ROMAN = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100
}

ROMAN_REV = {
    ('I', 'V'): 3,
    ('I', 'X'): 8,
    ('X', 'L'): 30,
    ('X', 'C'): 80,
}


def check_valid(number: str):
    for ch in number:
        if ch not in ROMAN:
            return True

    return False


def from_roman_numerals(args):
    number = args.roman_str
    prev = None
    sum_ = 0

    is_not_valid = check_valid(number)
    if is_not_valid:
        raise ValueError

    for ch in number:
        if prev and ROMAN[prev] < ROMAN[ch]:
            sum_ += ROMAN_REV[(prev, ch)]
        else:
            sum_ += ROMAN[ch]
        prev = ch

    return sum_


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('roman_str', type=str, help='Roman number')
    args = parser.parse_args()
    print(from_roman_numerals(args))


if __name__ == "__main__":
    main()
