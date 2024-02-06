#!/usr/bin/python3
'''read file'''
import json
from sys import argv
from os import path


def save_to_json_file(my_obj, filename):
    '''save'''
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    '''load'''
    with open(filename, 'r', encoding='utf-8') as f:
        res = json.load(f)
    return res


FILENAME = 'add_item.json'
file_content = []

if path.isfile(FILENAME):
    file_content = load_from_json_file(FILENAME)

for i in argv[1:]:
    file_content.append(i)

save_to_json_file(file_content, FILENAME)

# print(load_from_json_file('6-test.json'))
