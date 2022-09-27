#!/usr/bin/python3
"""Reads a file"""


def read_file(filename=""):
    """Reads the given file"""

    f = open(filename, "r")
    print(f.read())
