#!/usr/bin/python3
def print_last_digit(number):
    number = number if number > 0 else -number
    print(number % 10, end='')
    return number % 10
