#!/usr/bin/python3
"""Module that adds two integers"""


def add_integer(a, b=98):
    """Add two integers or floats (casted to integers)

    Args:
        a: first number
        b: second number, default 98

    Returns:
        The sum of a and b as an integer
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
