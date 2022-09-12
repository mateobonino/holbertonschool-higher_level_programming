#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx > len(my_list):
        return my_list
    elif idx < 0:
        ret_list = list(my_list)
        return new_list
    else:
        ret_list = list(my_list)
        i = 0
        while i <= idx:
            if i == idx:
                ret_list[i] = element
                return ret_list
            else:
                i += 1
