#!/usr/bin/python3
"""Module that defines an empty class BaseGeometry."""


class BaseGeometry:
    """class defined BaseGeometry."""
    def area(self):
        """Raises an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that 'value' is a positive integer."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""Module that defines a class Rectangle that inherits from BaseGeometry."""


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


"""Module that defines a class Square that inherits from Rectangle."""


class Square(Rectangle):
    """A class that defines a square."""

    def __init__(self, size):
        """Initializes the square with size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square."""
        return (self.__size * self.__size)
