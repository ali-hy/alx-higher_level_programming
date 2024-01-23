#!/usr/bin/python3
"""Square"""


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)) -> None:
        """init square"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """access position"""
        return self.__position

    @position.setter
    def position(self, val):
        """set position"""
        if not isinstance(val, tuple) \
           or len(val) != 2 or type(val[0]) != int or type(val[1]) != int \
            val[0] < 0 or val[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = val

    def my_print(self):
        """print square"""
        if self.size == 0:
            print('')
            return

        print('\n'*self.position[1], end='')
        for _ in range(self.size):
            print(' '*self.position[0] + '#'*self.size)
