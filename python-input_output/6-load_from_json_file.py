#!/usr/bin/python3
"""Converts json to object"""

import json


def save_to_json_file(my_obj, filename):
    """Creates an object from a JSON file"""
    with open(filename, "a") as f:
        return json.load(f)
    f.close()
