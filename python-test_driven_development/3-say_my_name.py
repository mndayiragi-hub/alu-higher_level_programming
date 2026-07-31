#!/usr/bin/python3
"""Module that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """Print My name is <first name> <last name>

    Args:
        first_name: the first name (must be a string)
        last_name: the last name (must be a string), default empty

    Raises:
        TypeError: if first_name or last_name is not a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
