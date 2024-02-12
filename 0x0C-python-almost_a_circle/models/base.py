#!/usr/bin/python3
"""Module for Base class"""
import json


class Base:
    """
    Base class
    This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code (by extension, same bugs)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        '''Set automatic id or hard-coded id'''
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries=[]):
        if list_dictionaries == None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string=''):
        if json_string == None or json_string == '':
            json_string = '[]'
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs=[]):
        if list_objs == None:
            list_objs = []
        if not all(map(lambda obj: isinstance(obj, cls), list_objs)):
            raise TypeError(
                f"all objects in list_objs should be of type {cls}"
            )
        with open(f'{cls.__name__} .json', 'w') as f:
            list_dictionaries = [obj.to_dictionary() for obj in list_objs]
            f.write(Base.to_json_string(list_dictionaries))

    @classmethod
    def create(cls, **dictionary):
        obj = cls(1, 1)
        obj.update(**dictionary)

    @classmethod
    def load_from_file(cls):
        dictionaries = []
        with open(f'{cls.__name__}.json', 'r') as f:
            dictionaries = Base.from_json_string(f.read())
        res = [cls.create(dictionary) for dictionary in dictionaries]
        return res
