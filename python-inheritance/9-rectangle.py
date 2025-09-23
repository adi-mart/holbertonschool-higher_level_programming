#!/usr/bin/python3
"""Module that defines an empty class BaseGeometry."""


class BaseGeometry:
    """class defined BaseGeometry."""
    def area(self):
        """Raises an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that 'value' is a positive integer.
        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than or equal to 0.
        """
        if type(value) is not int or type(value) is bool:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A class that defines a rectangle."""
    def __init__(self, width, height):
        """Initializes the rectangle with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return (self.__width * self.__height)

    def __str__(self):
        """Returns the string representation of the rectangle."""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
