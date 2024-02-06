#!/usr/bin/python3
'''read file'''


class Student:
    '''student'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        serializable = {}

        if isinstance(attrs, list) and \
           all([isinstance(s, str) for s in attrs]):
            for attr, value in self.__dict__.items():
                if attr in attrs:
                    serializable[attr] = value
        else:
            for attr, value in self.__dict__.items():
                serializable[attr] = value

        return serializable

    def reload_from_json(self, json):
        for attr, value in json.items():
            self.__dict__[attr] = value
