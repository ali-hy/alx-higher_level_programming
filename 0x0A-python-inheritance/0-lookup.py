#!/usr/bin/python3
'''lookup'''


def lookup(obj):
    '''get all attributes and methods of a n object'''
    return dir(obj)

print(lookup('hehe lol'))
