#!/usr/bin/python3
'''read file'''


def read_file(filename=""):
    '''read all the entire file with the name <filename>'''
    res = ''
    with open(filename, 'r', encoding='utf-8') as f:
        res = f.read()
    print(res)

read_file('0-test.txt')
