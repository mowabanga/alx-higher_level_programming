#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
zero = number % 1000
if zero == 0:
	print(f"Last digit of {number} is {zero} and is 0")
if zero > 5:
	print(f"Last digit of {number} is {zero} and is greater than 5")
if zero < 6 and zero != 0:
	print(f"Last digit of {number} is {zero} and is less than 6 and not 0")
