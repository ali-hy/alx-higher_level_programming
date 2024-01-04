#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    res = 0
    for arg in argv:
        res += int(arg)
    print(res)
