#!/usr/bin/python3
"""Appends text to a file"""


def append_write(filename="", text=""):
    """Appends text to the given file"""

    with open(filename, "a") as f:
        return f.write(text)
    f.close()
