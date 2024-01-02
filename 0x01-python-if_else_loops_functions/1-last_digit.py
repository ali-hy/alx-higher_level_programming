#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

def get_last_dig(num):
    if num >= 0:
        return num % 10
    return -((-num) % 10)

note = ''
if number == 0:
    note = '0'
elif number > 5:
    note = 'greater than 5'
else:
    note = 'less than 6 and not 0'
print(f"Last digit of {number} is {get_last_dig(number)} and is {note}")
