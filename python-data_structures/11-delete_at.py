#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    new_list = my_list
    for i in range(0, len(my_list), 1):
        if i == idx:
            del my_list[i]
            return new_list
