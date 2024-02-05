#!/usr/bin/python3
'''base geometry'''


class BaseGeometry:
    '''Base Geometry class'''
    def area(self):
        '''placeholder for area function in child classes'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''check if `value` is a valid integer
        name: name of this integer (for error message)
        value: value of integer (to validate)'''
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
