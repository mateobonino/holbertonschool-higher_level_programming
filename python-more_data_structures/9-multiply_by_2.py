#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mul = 0
    ret_dic = a_dictionary.copy()
    for k in a_dictionary.keys():
        mul = a_dictionary[k] * 2
        ret_dic.update({a_dictionary[k]: mul})
