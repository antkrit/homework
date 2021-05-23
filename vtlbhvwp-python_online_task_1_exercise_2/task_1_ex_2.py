"""01-Task1-Task2
Write a Python-script that performs the standard math functions on the data. The name of function and data are
set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py add 1 2

Notes:
Function names must match the standard mathematical, logical and comparison functions from the built-in libraries.
The script must raises all happened exceptions.
For non-mathematical function need to raise NotImplementedError.
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""
import argparse
import operator
import math


def calculate(args):

    if hasattr(math, args.operation):
        return getattr(math, args.operation)(*args.numbers)
    elif hasattr(operator, args.operation):
        return getattr(operator, args.operation)(*args.numbers)

    raise NotImplementedError


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", type=str, help="operation to be performed")
    parser.add_argument("numbers", type=float, nargs='+', help="left operand")
    args = parser.parse_args()

    print(calculate(args))


if __name__ == '__main__':
    main()
