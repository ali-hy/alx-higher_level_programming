#!/usr/bin/python3
def fizzbuzz():
    fizzstop = 3
    buzzstop = 5

    for i in range(101):
        number = True
        if i % fizzstop == 0:
            print('Fizz', end='')
            number = False
        if i % buzzstop == 0:
            print('Buzz', end='')
            number = False
        if number:
            print(i, end='')
        print(' ', end='')

fizzbuzz()
