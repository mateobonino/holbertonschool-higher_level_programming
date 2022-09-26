#!/usr/bin/python3
"""MyList Class"""


class MyList(list):
    """Class that inherits from the class 'list'"""

    def print_sorted(self):
        print(sorted(self))
