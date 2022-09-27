#!/usr/bin/python3
"""Writes to a file"""


def write_file(filename="", text=""):
    """Writes to the given file"""

    with open(filename, "a") as f:
        f.write(text)
    f.close()