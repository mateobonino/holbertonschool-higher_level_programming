#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list or len(my_list) == 0:
        return None
    max_int = 0
    for i in range(0, len(my_list), 1):
        if my_list[i] > max_int:
            if my_list[i] >= 0:
                max_int = my_list[i]
            else:
                max_int = (my_list[i] * -1)
    return max_int
