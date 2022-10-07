#!/usr/bin/python3
"""Base class"""


import json
import os


class Base():
    """Base clase"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Square":
            inst = cls(1)
        elif cls.__name__ == "Rectangle":
            inst = cls(1, 1)
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        fname = cls.__name__ + '.json'
        if os.path.exists(fname):
            with open(fname, 'r') as f:
                instances_l = []
                json_list = cls.from_json_string(f.read())
                for i in json_list:
                    instances_l.append(cls.create(**i))
                return instances_l
        else:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is not None:
            fname = cls.__name__ + '.json'
            listtt = []
            for i in list_objs:
                listtt.append(i.to_dictionary())
            with open(fname, "w+") as f:
                f.write(Base.to_json_string(listtt))
                return f.read()