#!/usr/bin/python3
"""
Module defining an abstract base class for geometric shapes and
concrete subclasses for Circle and Rectangle.

This module demonstrates the use of abstract base classes (ABC)
and duck typing in Python.
It provides a blueprint for shapes and allows handling of different
shape objects uniformly.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for geometric shapes.

    This class enforces the implementation of area and perimeter methods
    in all subclasses. It serves as a blueprint for any geometric shape.
    """
    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.

        This method must be implemented by all subclasses.

        Returns:
            float: The area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape.

        This method must be implemented by all subclasses.

        Returns:
            float: The perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Concrete class representing a circle.

    Inherits from Shape and implements area and perimeter
    calculations for a circle.
    """
    def __init__(self, radius):
        """
        Initialize a Circle instance.

        Args:
            radius (float): The radius of the circle.
        """
        self.__radius = abs(radius)

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return (math.pi * (self.__radius ** 2))

    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return (2 * math.pi * self.__radius)


class Rectangle(Shape):
    """
    Concrete class representing a rectangle.

    Inherits from Shape and implements area and perimeter
    calculations for a rectangle.
    """
    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.__width = abs(width)
        self.__height = abs(height)

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return (2 * (self.__width + self.__height))


def shape_info(obj):
    """
    Print the area and perimeter of a shape object.

    This function uses duck typing: it expects the object to have
    'area' and 'perimeter' methods, regardless of its actual class.

    Args:
        obj: Any object that implements area() and perimeter() methods.
    """
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")


if __name__ == "__main__":
    circle = Circle(radius=4)
    rectangle = Rectangle(width=2, height=6)
    shape_info(circle)
    shape_info(rectangle)
