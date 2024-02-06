#!/usr/bin/python3
import json
'''read file'''


def from_json_string(my_str):
    '''turn JSON-format <my_str> into an object'''
    return json.loads(my_str)
