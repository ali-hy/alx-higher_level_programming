#!/usr/bin/python3
'''just for a test'''
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import turtle

if __name__ == '__main__':
    r1 = Rectangle(20, 40, 50, 90)
    r2 = Rectangle(50, 40, 300, 200)

    s1 = Square(40, 100, 100)
    Base.draw([r1, r2], [s1])
