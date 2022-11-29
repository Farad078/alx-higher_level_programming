#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
x = number % 10
if (number >= 0):
    if (x > 5):
        print(f"Last digit of {number} is {x} and is greater than 5")
    elif (x == 0):
        print(f"Last digit of {number} is {x} and is 0")
    elif (x <= 5):
        print(f"Last digit of {number} is {x} and is less than 6 and not 0")

elif (number < 0):
    k = -1 * number
    y = -1 * (k % 10)
    print(f"Last digit of {number} is {y} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {y} and is 0")
