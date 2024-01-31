#!/usr/bin/python3
'''rectangle'''

class Rectangle:
    '''Rectangle'''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width__
    
    @width.setter
    def width(self, val):
        if (not isinstance(val, int)):
            raise TypeError('width must be an integer')
        if (val < 0):
            raise ValueError('width must be >= 0')
        self.__width__ = val
    
    @property
    def height(self):
        return self.__height__
    
    @height.setter
    def height(self, val):
        if (not isinstance(val, int)):
            raise TypeError('height must be an integer')
        if (val < 0):
            raise ValueError('height must be >= 0')
        self.__height__ = val
