#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
   last_num = number % 10
else:
   last_num = (((number * -1) % 10) ^ -1)
if last_num > 5:
   print("last digit of {} is {} and is greater than 5".format(number, last_num)
elif (last_num < 6) and (last_num != 0)
   print("last digit of {} is {} and is less than 6 and not 0".format(number, last_num)
elif last_num == 0:
   print("last digit of {} is {} and is 0".format(number, last_num)