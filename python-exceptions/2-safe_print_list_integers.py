#!/usr/bin/python3
from re import I


def safe_print_list_integers(my_list=[], x=0):
    num_printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num_printed += 1
        except:
            pass
    print("")
    return num_printed
