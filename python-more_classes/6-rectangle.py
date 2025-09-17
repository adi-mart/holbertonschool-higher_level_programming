#!/usr/bin/python3
"""Defines a rectangle."""


class Rectangle:
    """Represent a rectangle."""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            Rectangle.number_of_instances (int): The number of
            Rectangle instances.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle."""
        return (self.__height * self.__width)

    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """Returns the string representation of the rectangle with '#'."""
        if self.__width == 0 or self.__height == 0:
            return ("")
        result = ""
        for i in range(self.__height):
            result += "#" * self.__width
            if i != self.__height - 1:
                result += "\n"
        return (result)

    def __repr__(self):
        """Returns a string representation of the rectangle
        for reproduction."""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def eval(self):
        """Evaluates the rectangle."""
        return (self.__width * self.__height)

    def __del__(self):
        """Prints a message when a rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
