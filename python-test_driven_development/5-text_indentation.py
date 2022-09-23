#!/usr/bin/python3
"""Prints a text"""


def text_indentation(text):
    """Prints a text"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:" or text[i] == "\n":
            print("\n")
            i += 1
            while i < len(text) and (text[i] == ' ' or text[i] == '\t'):
                i += 1
            continue
        i += 1
    print()
