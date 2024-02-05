#!/usr/bin/python3
'''base geometry'''


class BaseGeometry:
    '''Base Geometry class'''
    def area(self):
        '''placeholder for area function in child classes'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Validate a parameter as an integer.
        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        '''
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    '''Rectangle'''
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return '[Rectangle] {:d}/{:d}'.format(self.__width, self.__height)


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
