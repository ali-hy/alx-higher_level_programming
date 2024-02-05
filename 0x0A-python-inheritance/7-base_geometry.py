#!/usr/bin/python3
'''base geometry'''


class BaseGeometry:
    '''Base Geometry class'''
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if not value.__class__ == int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
