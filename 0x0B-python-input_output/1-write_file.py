#!/usr/bin/python3
'''read file'''

def write_file(filename="", text=""):
    '''write <text> to file called <filename>'''
    res = 0
    with open(filename, 'w', encoding='utf-8') as f:
        res = f.write(text)
    return res
