#!/usr/bin/python3
"""Reads a file"""


def read_file(filename=""):
    """Reads the given file"""

    with open(filename, "r") as f:
        print(f.read(), end='')
    f.close()
