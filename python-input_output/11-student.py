#!/usr/bin/python3
"""Student Class"""


class Student():
    """Defines a Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        if isinstance(attrs, list):
            attributes = {}
            for i in attrs:
                if hasattr(self, i):
                    attributes[i] = getattr(self, i)
            return attributes

    def reload_from_json(self, json):
        self.__dict__.update(json)
