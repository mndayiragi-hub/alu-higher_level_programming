#!/usr/bin/python3
"""Module that defines the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Class that defines a rectangle, inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance

        Args:
            width: the width of the rectangle
            height: the height of the rectangle
            x: the x position, default 0
            y: the y position, default 0
            id: the id to assign, or None to auto-increment
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width"""
        self.__width = value

    @property
    def height(self):
        """Retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height"""
        self.__height = value

    @property
    def x(self):
        """Retrieve x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x"""
        self.__x = value

    @property
    def y(self):
        """Retrieve y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y"""
        self.__y = value
