#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx > len(my_list) - 1 or idx < 0:
        return my_list
    else:
        i = 0
        while i <= idx:
            if i == idx:
                my_list[i] = element
                return my_list
            else:
                i += 1