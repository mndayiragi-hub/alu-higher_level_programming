#!/usr/bin/python3
"""Module that defines the Base class"""

import json


class Base:
    """Base class that manages the id attribute for all future classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance

        Args:
            id: the id to assign, or None to auto-increment
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
