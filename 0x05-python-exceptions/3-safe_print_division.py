#!/usr/bin/python3
def safe_print_division(a, b):
    num = 0
    try:
        num = a/b
    except ZeroDivisionError:
        num = None
    finally:
        print("Inside result: {}".format(num))
    return num

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
