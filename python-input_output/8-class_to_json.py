#!/usr/bin/python3
"""Class to json module"""


def class_to_json(obj):
    """Returns the dictionary description for JSON"""
    return obj.__dict__
