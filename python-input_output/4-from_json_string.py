#!/usr/bin/python3
"""Converts to object string format"""

import json


def from_json_string(my_str):
    """Converts to String"""
    return json.load(my_str)
