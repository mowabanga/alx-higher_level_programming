#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
const = "Last digit of"
if last_digit > 5:
    print(f"{const} {number} is {last_digit} and is greater than 5")
elif last_digit != 0 and last_digit < 6:
    print(f"{const} {number} is {last_digit} and is less than 6 and not 0")
else:
    print(f"{const} {number} is {last_digit} and is 0")