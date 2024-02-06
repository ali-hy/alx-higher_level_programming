#!/usr/bin/python3
'''read file'''


def append_write(filename="", text=""):
    '''append <text> to file called <filename>'''
    res = 0
    with open(filename, 'a', encoding='utf-8') as f:
        res = f.write(text)
    return res
