#!/usr/bin/python3
import json
'''read file'''


def save_to_json_file(my_obj, filename):
    '''save'''
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)

# save_to_json_file({
#     'a': "that's the first letter",
#     'l': 2,
#     'i': True
# }, '5-test.py')
