"""
Task 2_3

You are given n bars of gold with weights: w1, w2, ..., wn and bag with capacity W.
There is only one instance of each bar and for each bar you can either take it or not
(hence you cannot take a fraction of a bar). Write a function that returns the maximum weight of gold that fits
into a knapsack's capacity.

The first parameter contains 'capacity' - integer describing the capacity of a knapsack
The next parameter contains 'weights' - list of weights of each gold bar
The last parameter contains 'bars_number' - integer describing the number of gold bars
Output : Maximum weight of gold that fits into a knapsack with capacity of W.

Note:
Use the argparse module to parse command line arguments. You don't need to enter names of parameters (i. e. -capacity)
Raise ValueError in case of false parameter inputs
Example of how the task should be called:
python3 task3_1.py -W 56 -w 3 4 5 6 -n 4
"""
import argparse


def bounded_knapsack(args):
    capacity = args.W
    weights = reversed(args.w)
    num = args.n
    sum_ = 0

    try:
        assert capacity > 0
        assert num > 0
    except AssertionError:
        raise ValueError

    for w in weights:
        if w < 0:
            raise ValueError
        elif sum_+w >= capacity:
            continue

        sum_ += w

    return sum_


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-W', nargs='?', type=float, help='capasity of a bag')
    parser.add_argument('-w', nargs='+', type=float, help='weights')
    parser.add_argument('-n', nargs='?', type=int, help='number of gold bars')
    args = parser.parse_args()

    print(bounded_knapsack(args))


if __name__ == '__main__':
    main()
