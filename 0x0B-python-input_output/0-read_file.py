#!/usr/bin/python3
'''read file'''

def read_file(filename=""):
    '''read all the entire file with the name <filename>'''
    res = ''
    with open(filename, 'r', encoding='utf-8') as f:
        res = '\n'.join(f.readlines())
    return res
