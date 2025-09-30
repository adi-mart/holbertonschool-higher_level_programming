#!/usr/bin/python3
"""
Module that contains a Student class
"""


class Student:
    """
    Class that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance

        Args:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieve a dictionary representation of a Student instance

        Returns:
            dict: dictionary representation of the student
        """
        return (self.__dict__)
