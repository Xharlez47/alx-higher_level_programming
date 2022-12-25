#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    firstnums = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            firstnums += 1
        except TypeError:
            continue
    print()
    return firstnums
