#!/usr/bin/python3
"""Converts to object string format"""

import json


def save_to_json_file(my_obj, filename):
    """Converts to String"""
    with open(filename, "a") as f:
        f.write(json.dumps(my_obj))
