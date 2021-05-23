"""01-Task1-Task1
Write a Python-script that performs simple arithmetic operations: '+', '-', '*', '/'. The type of operator and
data are set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py 1 * 2

Notes:
For other operations need to raise NotImplementedError.
Do not dynamically execute your code (for example, using exec()).
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""


import argparse

OPERATORS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}


def check(args):
    if args.operation not in OPERATORS.keys():
        raise NotImplementedError

    return OPERATORS[args.operation](float(args.number_right), float(args.number_left))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("number_right", type=float, help="left operand")
    parser.add_argument("operation", type=str, help="operation to be performed")
    parser.add_argument("number_left", type=float, help="right operand")
    args = parser.parse_args()

    print(check(args))


if __name__ == '__main__':
    main()