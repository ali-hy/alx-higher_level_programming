#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
note = ''
if number == 0:
    note = '0'
elif number > 5:
    note = 'greater than 5'
else:
    note = 'less than 6 and not 0'
print(f"Last digit of {number} is {number % 10} and is {note}")
