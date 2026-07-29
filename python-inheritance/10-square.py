#!/usr/bin/python3
"""Module that defines a Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that defines a square, inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a new Square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
