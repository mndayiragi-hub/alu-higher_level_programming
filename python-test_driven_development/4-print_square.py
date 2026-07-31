#!/usr/bin/python3
"""Module that prints a square with the character #"""


def print_square(size):
    """Print a square of size using the character #

    Args:
        size: the size length of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
