""" Write a Python-script that determines whether the input string is the correct entry for the
'formula' according EBNF syntax (without using regular expressions).
Formula = Number | (Formula Sign Formula)
Sign = '+' | '-'
Number = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
Input: string
Result: (True / False, The result value / None)

Example,
user_input = '1+2+4-2+5-1' result = (True, 9)
user_input = '123' result = (True, 123)
user_input = 'hello+12' result = (False, None)
user_input = '2++12--3' result = (False, None)
user_input = '' result = (False, None)

Example how to call the script from CLI:
python task_1_ex_3.py 1+5-2

Hint: use argparse module for parsing arguments from CLI
"""
import argparse


def check_formula(user_input):
    ebnf_arr = user_input.split('+')

    for i, ch in enumerate(ebnf_arr):
        ebnf_arr[i] = ch.split('-')

    rez = 0
    try:
        for itm in ebnf_arr:
            sum_ = int(itm[0])
            for i in range(1, len(itm)):
                sum_ -= int(itm[i])
            rez += sum_
    except ValueError:
        return False, None
    else:
        return True, rez


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("user_input", help="Extended Backus-Naur form")
    args = parser.parse_args()
    print(check_formula(args.user_input))


if __name__ == '__main__':
    main()
