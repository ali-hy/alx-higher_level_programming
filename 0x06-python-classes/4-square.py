#!/usr/bin/python3
"""Square"""


class Square:
    """Square class"""

    def __init__(self, size=0) -> None:
        """init square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns area of square"""
        return self.__size * self.__size
    
    @property
    def size(self):
        """access private property"""
        return self.__size
