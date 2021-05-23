"""
Develop Rectangle class with following content:
    2 private fields type of float `side_a` and `side_b` (sides А and В of the rectangle);
    One constructor with two optional parameters a and b (parameters specify rectangle sides). Side А of a rectangle
    defaults to 4, side В - 3. Raise ValueError if received parameters are less than or equal to 0;
    Method `get_side_a`, returning value of the side А;
    Method `get_side_b`, returning value of the side В;
    Method `area`, calculating and returning the area value;
    Method `perimeter`, calculating and returning the perimeter value;
    Method `is_square`, checking whether current rectangle is square or not. Returns True if the shape is square and
    False in another case;
    Method `replace_sides`, swapping rectangle sides.

Develop class ArrayRectangles, in which declare:
    Private attribute `rectangle_array` (list of rectangles);
    One constructor that creates a list of rectangles with length `n` filled with `None` and that receives an
    arbitrary amount of objects of type `Rectangle` or a list of objects of type `Rectangle` (the list must be
    unpacked inside the constructor so that there will be no nested arrays). If both objects and length are passed,
    at first creates a list with received objects and then add the required number of Nones to achieve the
    desired length. If `n` is less than the number of received objects, the length of the list will be equal to the
    number of objects;
    Method `add_rectangle` that adds a rectangle of type `Rectangle` to the array on the nearest free place and
    returning True, or returning False, if there is no free space in the array;
    Method `number_max_area`, that returns order number (index) of the first rectangle with the maximum area value
    (numeration starts from zero);
    Method `number_min_perimeter`, that returns order number (index) of the first rectangle with the minimum area value
    (numeration starts from zero);
    Method `number_square`, that returns the number of squares in the array of rectangles
"""


class Rectangle:
    def __init__(self, a=4, b=3):
        if a <= 0 or b <= 0:
            raise ValueError

        self.__side_a = a
        self.__side_b = b

    def get_side_a(self):
        return self.__side_a

    def get_side_b(self):
        return self.__side_b

    def area(self):
        return self.__side_a * self.__side_b

    def perimeter(self):
        return 2 * (self.__side_a + self.__side_b)

    def is_square(self) -> bool:
        return self.__side_a == self.__side_b

    def replace_sides(self) -> None:
        self.__side_a, self.__side_b = self.__side_b, self.__side_a


class ArrayRectangles:
    def __init__(self, *args, n=0):
        self.__rectangle_array = list()

        for item in args:
            if isinstance(item, (tuple, list)):
                self.__rectangle_array.extend(item)
            elif isinstance(item, Rectangle):
                self.__rectangle_array.append(item)
            else:
                raise ValueError

        if (curr_n := len(self.__rectangle_array)) < n:
            self.__rectangle_array.extend([None]*(n-curr_n))

    def add_rectangle(self, rec: Rectangle) -> bool:
        for i, item in enumerate(self.__rectangle_array):
            if item is None:
                self.__rectangle_array[i] = rec
                return True

        return False

    def number_max_area(self) -> int:
        return self.__rectangle_array.index(max(list(filter(None, self.__rectangle_array)), key=Rectangle.area))

    def number_min_perimeter(self) -> int:
        return self.__rectangle_array.index(min(list(filter(None, self.__rectangle_array)), key=Rectangle.perimeter))

    def number_square(self) -> int:
        return len([item for item in self.__rectangle_array if item and item.is_square()])
