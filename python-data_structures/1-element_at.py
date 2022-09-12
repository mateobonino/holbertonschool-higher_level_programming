#!/usr/bin/python3
def element_at(my_list, idx):
    if idx > len(my_list) - 1 or idx < 0:
        return None
    else:
        i = 0
        while i <= idx:
            if i == idx:
                return my_list[i]
            else:
                i += 1
