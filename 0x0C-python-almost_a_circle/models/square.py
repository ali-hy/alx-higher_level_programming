#!/usr/bin/python3
'''Module for the Square Class'''
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Class representing a square'''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        '''updates rectangle attributes
        args must not be more than 5
        enter args in the following order:
        [id, size, x, y]

        if no args are entered kwargs will be used'''
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for i in range(0, min(len(attrs), len(args))):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        '''Returns string with the format
        [Square] (<id>) <x>/<y> - <size>'''
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'


    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

if __name__ == '__main__':
    s = Square(5)
    print(s.__dict__)
    setattr(s, 'size', 3)
    print(s.__dict__)
