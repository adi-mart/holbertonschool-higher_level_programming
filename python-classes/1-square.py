#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """A class that defines a square by its size."""
    __size = None

    def __init__(self, size):
        """Initialize the square with a given size."""
        self.__size = size
