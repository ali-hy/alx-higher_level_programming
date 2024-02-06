#!/usr/bin/python3
'''read file'''
import json
from sys import argv
from os import path


def class_to_json(obj):
    '''return a JSON string representing all serializable attributes of
    <obj>'''
    serializable = {}
    for attr, value in obj.__dict__.items():
        serializable[attr] = value

    return serializable
