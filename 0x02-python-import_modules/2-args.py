#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:")
        print("{}: {}".format(1, argv[1]))
    else:
        print("{} arguments:".format(len(argv) - 1))
        for i in len(argv):
            print("{}: {}".format(i, argv[i]))
