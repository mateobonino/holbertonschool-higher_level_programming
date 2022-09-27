#!/usr/bin/python3
"""Converts json to object"""

import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file"""
    with open(filename, "a") as f:
        return json.load(f)
    f.close()
