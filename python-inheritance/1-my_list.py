#!/usr/bin/python3
"""Module that defines a class MyList that inherits from list."""


class MyList(list):
    """A class that inherits from list."""
    def print_sorted(self):
        """Prints the list in sorted (ascending) order."""
        print(sorted(self))
