"""
Write 2 functions:
1. Function 'is_sorted', determining whether a given list of integer values of arbitrary length
is sorted in a given order (the order is set up by enum value SortOrder).
List and sort order are passed by parameters. Function does not change the array, it returns
boolean value.

2. Function 'transform', replacing the value of each element of an integer list with the sum
of this element value and its index, only if the given list is sorted in the given order
(the order is set up by enum value SortOrder). List and sort order are passed by parameters.
To check, if the array is sorted, the function 'is_sorted' is called.

Example for 'transform' function,
For [5, 17, 24, 88, 33, 2] and “ascending” sort order values in the array do not change;
For [15, 10, 3] and “ascending” sort order values in the array do not change;
For [15, 10, 3] and “descending” sort order the values in the array are changing to [15, 11, 5]

Note:
Raise TypeError in case of wrong function arguments data type;
"""
from enum import Enum
from typing import List


class SortOrder(Enum):
    ASC = 'ascending'
    DESC = 'descending'


def is_sorted(num_list: List[int], sort_order: SortOrder) -> bool:
    try:
        assert isinstance(num_list, list)
        assert isinstance(sort_order, SortOrder)
        to_reverse = (sort_order.value == 'descending')
        return sorted(num_list, reverse=to_reverse) == num_list

    except AssertionError:
        raise TypeError


def transform(num_list: List[int], sort_order: SortOrder) -> List[int]:

    try:
        assert isinstance(num_list, list)
        assert isinstance(sort_order, SortOrder)

        if is_sorted(num_list, sort_order):
            for i, x in enumerate(num_list):
                num_list[i] = x+i

        return num_list
    except AssertionError:
        raise TypeError
