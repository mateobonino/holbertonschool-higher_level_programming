#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ret_dic = a_dictionary.copy()
    return ret_dic.update({n: 2 * ret_dic[n] for n in ret_dic.keys()})
