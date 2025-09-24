#!/usr/bin/python3
"""Module defining an abstract base class for shapes and
concrete subclasses for Circle and Rectangle."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""
    @abstractmethod
    def area(self):
        """Abstract method to be implemented by subclasses
        to return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to be implemented by subclasses
        to return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Concrete class for circles."""
    def __init__(self, radius):
        """Initialize a Circle with a given radius."""
        self.__radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return (math.pi * (self.__radius ** 2))

    def perimeter(self):
        """Calculate the perimeter (circumference) of the circle."""
        return (2 * math.pi * self.__radius)


class Rectangle(Shape):
    """Concrete class for rectangles."""
    def __init__(self, width, height):
        """Initialize a Rectangle with a given width and height."""
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return (2 * (self.__width + self.__height))


def shape_info(obj):
    """Print the area and perimeter of a shape object."""
    print("Area: {}".format(obj.area()))
    print("Perimeter: {}".format(obj.perimeter()))
