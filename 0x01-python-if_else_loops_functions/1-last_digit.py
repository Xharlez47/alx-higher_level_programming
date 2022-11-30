#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_num = number % 10
else:
    last_num = (((number * -1) % 10) * -1)
print("Last digit of {}".format(number), end=' ')
if last_num > 5:
    print("is {} and is greater than 5".format(last_num))
elif last_num == 0:
    print("is {} and is 0".format(last_num))
elif last_num < 6 and last_num != 0:
    print("is {} and is less than 6 and not 0".format(last_num))
