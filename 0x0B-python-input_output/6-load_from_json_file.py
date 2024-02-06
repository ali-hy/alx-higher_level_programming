#!/usr/bin/python3
import json
'''read file'''


def load_from_json_file(filename):
    '''load'''
    with open(filename, 'r', encoding='utf-8') as f:
        res = json.load(f)
    return res

# print(load_from_json_file('6-test.json'))
