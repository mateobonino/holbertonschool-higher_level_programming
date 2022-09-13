#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dc_copy = a_dictionary.copy()
    mul = 0
    for k in a_dictionary:
        mul = a_dictionary[k] * 2
        dc_copy = dc_copy.replace({a_dictionary[k], mul})
    return dc_copy
