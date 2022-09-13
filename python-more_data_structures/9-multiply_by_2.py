#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mult = 0
    for i in a_dictionary:
        mult *= a_dictionary[i]
    return mult
