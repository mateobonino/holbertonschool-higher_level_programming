#!/usr/bin/python3
"""Converts json to object"""

import json


def save_to_json_file(my_obj, filename):
    """Converts json to an object"""
    with open(filename, "a") as f:
        return json.load(f)
    f.close()
