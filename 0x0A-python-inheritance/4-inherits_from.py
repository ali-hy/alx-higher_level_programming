#!/usr/bin/python3
'''check same class'''


def inherits_from(obj, a_class):
    '''check if obj inherits from a_class'''
    if isinstance(obj, a_class):
        return False
    return issubclass(obj.__class__, a_class)
