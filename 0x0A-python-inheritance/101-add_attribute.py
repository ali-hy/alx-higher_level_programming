#!/usr/bin/python3
'''my rebelious int'''


def add_attribute(obj, attr, value):
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")

