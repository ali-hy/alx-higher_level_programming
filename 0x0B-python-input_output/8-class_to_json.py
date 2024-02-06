#!/usr/bin/python3
import json
from sys import argv
from os import path
'''read file'''


def class_to_json(obj):
    '''return a JSON string representing all serializable attributes of
    <obj>'''
    serializable = {}
    for attr, value in obj.__dict__.items():
        serializable[attr] = value

    return serializable
