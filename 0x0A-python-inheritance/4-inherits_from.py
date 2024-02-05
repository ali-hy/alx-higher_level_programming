#!/usr/bin/python3
'''check same class'''


def is_kind_of_class(obj, a_class):
    '''is_kind_of_class
    >>> is_kind_of_class(True, int)
    True
    >>> is_kind_of_class(A(), A)
    True
    >>> is_kind_of_class(B(), A)
    True
    >>> is_kind_of_class(34, A)
    False
    '''
    return issubclass(obj.__class__, a_class)
