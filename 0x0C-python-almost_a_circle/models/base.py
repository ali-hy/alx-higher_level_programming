#!/usr/bin/python3
"""Module for Base class"""
import json
import csv
import turtle


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
        '''Turn list of dictionaries into a json-format string'''
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string=''):
        '''Get a list of dictionaries from a json-format string'''
        if json_string is None or json_string == '':
            json_string = '[]'
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs=[]):
        '''save a list of objects to a file as json-format string
        that represents a list of dictionaries'''
        if list_objs is None:
            list_objs = []
        if not all(map(lambda obj: isinstance(obj, cls), list_objs)):
            raise TypeError(
                f"all objects in list_objs should be of type {cls}"
            )
        with open(f'{cls.__name__}.json', 'w') as f:
            list_dictionaries = [obj.to_dictionary() for obj in list_objs]
            f.write(Base.to_json_string(list_dictionaries))

    @classmethod
    def create(cls, **dictionary):
        '''create an object of the same class using the dictionary values'''
        if cls.__name__ == 'Square':
            obj = cls(1)
        else:
            obj = cls(1, 1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        '''load list of objects from file for the same class'''
        dictionaries = []
        try:
            with open(f'{cls.__name__}.json', 'r') as f:
                dictionaries = Base.from_json_string(f.read())
        except FileNotFoundError:
            return []
        res = [cls.create(**dictionary) for dictionary in dictionaries]
        return res

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''save list of objects to a csv file'''
        with open(f'{cls.__name__}.csv', 'w') as file:
            writer = csv.writer(file)
            if cls.__name__ == 'Square':
                attrs = ['id', 'size', 'x', 'y']
                rows = map(
                    lambda obj: [obj.id, obj.size, obj.x, obj.y],
                    list_objs
                )
            else:
                attrs = ['id', 'width', 'height', 'x', 'y']
                rows = map(
                    lambda obj: [obj.id, obj.width, obj.height, obj.x, obj.y],
                    list_objs
                )
            writer.writerow(attrs)
            writer.writerows(rows)

    @classmethod
    def load_from_file_csv(cls):
        '''load list of objects to a csv file'''
        res = []
        try:
            with open(f'{cls.__name__}.csv') as file:
                reader = csv.DictReader(file)
                for dictionary in reader:
                    dictionary = {
                        k: int(v) for k, v in dictionary.items()
                    }
                    res.append(cls.create(**dictionary))
        except FileNotFoundError:
            return []
        return res

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''draw a list of rectangles and a list of squares
        in a screen using the turtle module'''
        screen = turtle.Screen()
        screen.setup(500, 500)
        pen = turtle.RawTurtle(screen)

        pen.up()

        for rect in list_rectangles:
            pen.goto(rect.x, rect.y)
            pen.down()
            pen.fd(rect.width)
            pen.left(90)
            pen.fd(rect.height)
            pen.left(90)
            pen.fd(rect.width)
            pen.left(90)
            pen.fd(rect.height)
            pen.left(90)
            pen.up()
        for square in list_squares:
            pen.goto(square.x, square.y)
            pen.down()
            pen.fd(square.size)
            pen.left(90)
            pen.fd(square.size)
            pen.left(90)
            pen.fd(square.size)
            pen.left(90)
            pen.fd(square.size)
            pen.left(90)
            pen.up()

        turtle.done()


