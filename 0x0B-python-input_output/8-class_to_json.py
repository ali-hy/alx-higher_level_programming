#!/usr/bin/python3
import json
from sys import argv
from os import path
'''read file'''

def class_to_json(obj):
    '''return a JSON string representing all serializable attributes of <obj>'''
    serializable = {}
    for attr, value in obj.__dict__.items():
        serializable[attr] = value

    return json.dumps(serializable)

class MyClass:
    """ My class
    """

    score = 0

    def __init__(self, name, number = 4):
        self.__name = name
        self.number = number
        self.is_team_red = (self.number % 2) == 0

    def win(self):
        self.score += 1

    def lose(self):
        self.score -= 1

    def __str__(self):
        return "[MyClass] {} - {:d} => {:d}".format(self.__name, self.number, self.score)

m = MyClass("John")
m.win()
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)
