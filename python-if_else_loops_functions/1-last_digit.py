#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
if number < 0:
    ld = -ld
print(f"Last digit of {number} is {ld} ", end="")
if abs(number % 10) > 5:
    print("and is greater than 5")
elif abs(number % 10) == 0:
    print("and is 0")
elif abs(number % 10) < 6:
    print("and is less than 6 and not 0")
