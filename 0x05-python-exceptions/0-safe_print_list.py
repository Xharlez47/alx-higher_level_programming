#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    listTotal = 0
    for index in range(x):
        try:
            print("{}".format(mylist[index], end="")
            listTotal += 1
        except IndexError:
            break
     print("")
     return (listTotal)
