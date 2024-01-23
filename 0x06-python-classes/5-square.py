#!/usr/bin/python3
"""Square"""


class Square:
    """Square class"""

    def __init__(self, size=0) -> None:
        """init square"""
        self.size = size

    def area(self):
        """returns area of square"""
        return self.__size * self.__size

    @property
    def size(self):
        """access size property"""
        return self.__size

    @size.setter
    def size(self, val):
        """set size property"""
        if type(val) is not int:
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val

    def my_print(self):
        """print square"""
        if self.size == 0:
            print('')
            return

        for i in range(self.size):
            print('#'*self.size)
