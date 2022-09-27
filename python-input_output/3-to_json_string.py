#!/usr/bin/python3
"""Converts to JSON string format"""

import json


def to_json_string(my_obj):
    """Converts to JSON"""
    return json.dump(my_obj)
