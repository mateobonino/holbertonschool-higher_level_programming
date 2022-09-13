#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ret_dic = a_dictionary.copy()
    return ret_dic.update((x, y * 2) for x, y in ret_dic.items())
