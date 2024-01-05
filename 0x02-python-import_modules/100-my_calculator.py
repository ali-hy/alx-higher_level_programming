#!/usr/bin/python3
from calculator_1 import mul, div, add, sub
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    
    operations = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }

    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])
    
    if op not in operations:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    print("{:d} {} {:d} = {:d}".format(a, op, b, operations[op](a, b)))
