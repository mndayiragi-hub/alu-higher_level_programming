#!/usr/bin/python3
"""Module that defines the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that defines a square, inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance

        Args:
            size: the size of the square (used for width and height)
            x: the x position, default 0
            y: the y position, default 0
            id: the id to assign, or None to auto-increment
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
