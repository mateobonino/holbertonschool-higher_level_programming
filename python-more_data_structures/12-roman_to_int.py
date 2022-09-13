#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    rn = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    res = []

    for i in roman_string:
        for j in rn.keys():
            if i == j:
                res.append(rn.get(j))
    if len(res) > 1:
        for k in range(len(res) - 1):
            if res[k] < res[k + 1]:
                res[k] = -res[k]
    return sum(res)
