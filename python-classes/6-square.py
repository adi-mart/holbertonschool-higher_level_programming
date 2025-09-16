#!/usr/bin/python3
class Square:
    """A class that defines a square by its size."""
    __size = None

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with a given size and position."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set the position of the square with validation."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the '#' character considering its position."""
        if self.__size == 0:
            print()
        for i in range(self.position[1]):
            print(" ")
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
