#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list or len(my_list) == 0:
        return None
    max_int = my_list[0]
    for i in range(0, len(my_list), 1):
        if my_list[i] > max_int:
            max_int = my_list[i]
    return max_int
