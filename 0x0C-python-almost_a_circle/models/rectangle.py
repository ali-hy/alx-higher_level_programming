#!/usr/bin/python3
'''Module for the Rectangle Class'''
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from models.base import Base

class Rectangle(Base):
    '''Basic Rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        '''calculate rectangle's area'''
        return self.width * self.height

    def display(self):
        '''prints a rectangle to stdout using the # character'''
        print('\n'*self.y +
              '\n'.join([' ' * self.x + '#'*self.width] * self.height))

    def update(self, *args, **kwargs):
        '''updates rectangle attributes
        args must not be more than 5
        enter args in the following order:
        [id, width, height, x, y]

        if no args are entered kwargs will be used'''
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i in range(0, min(len(attrs), len(args))):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        '''create a dictionary that represents Rectangle object'''
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self) -> str:
        '''returns a string of the following format:
        [Rectangle] (<id>) <x>/<y> - <width>/<height>'''
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.x, self.y, self.width, self.height
        )

    @staticmethod
    def assertIsInteger(value, name):
        '''check if a value is an integer. If not, raise a TypeError'''
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')

    @staticmethod
    def assertIsPositiveInteger(value, name):
        '''check if a value is a positive integer. If not, raise a
        ValueError'''
        Rectangle.assertIsInteger(value, name)
        if value <= 0:
            raise ValueError(f'{name} must be > 0')

    @staticmethod
    def assertIsNonNegativeInteger(value, name):
        '''check if a value is a non-negative integer (>= 0). if not, raise
        a ValueError'''
        Rectangle.assertIsInteger(value, name)
        if value < 0:
            raise ValueError(f'{name} must be >= 0')

    @property
    def width(self):
        '''width of the rectangle
        range: must be > 0'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width of the rectangle
        range: must be > 0'''
        Rectangle.assertIsPositiveInteger(value, 'width')
        self.__width = value

    @property
    def height(self):
        '''height of the rectangle
        range: must be > 0'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height of the rectangle
        range: must be > 0'''
        Rectangle.assertIsPositiveInteger(value, 'height')
        self.__height = value

    @property
    def x(self):
        '''x cooridnate of the rectangle
        range: must be >= 0'''
        return self.__x

    @x.setter
    def x(self, value):
        '''x coordinate of the rectangle
        range: must be >= 0'''
        Rectangle.assertIsNonNegativeInteger(value, 'x')
        self.__x = value

    @property
    def y(self):
        '''y coordinate of the rectangle
        range: must be >= 0'''
        return self.__y

    @y.setter
    def y(self, value):
        '''y coordinate of the rectangle
        range: must be >= 0'''
        Rectangle.assertIsNonNegativeInteger(value, 'y')
        self.__y = value

