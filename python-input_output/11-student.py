#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation."""
        if type(attrs) is list:
            result = {}
            for key in attrs:
                if key in self.__dict__:
                    result[key] = self.__dict__[key]
            return result
        return self.__dict__

    def reload_from_json(self, json):
        """Replace attributes from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
