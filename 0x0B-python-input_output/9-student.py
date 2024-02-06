#!/usr/bin/python3
import json
from sys import argv
from os import path
'''read file'''

class Student:
    '''student'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        serializable = {}
        for attr, value in self.__dict__.items():
            serializable[attr] = value

        return serializable

s = Student('ali', 'haitham', 19)

print(s.to_json())
