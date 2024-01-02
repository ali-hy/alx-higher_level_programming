#!/usr/bin/python3
def islower(c):
    if (ord(c) >= ord('a') and ord('c') <= ord('z')):
        return True
    return False


def toupper(c):
    if islower(c):
        return chr(ord(c) + (ord('A') - ord('a')))
    return c


def uppercase(str):
    for c in str:
        print("{}".format(toupper(c)), end='')
    print('\n', end='')
