#!/usr/bin/python3
"""
Module that contains a Student class with reload functionality
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
        pass
    
    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance
        
        Args:
            attrs (list): list of attribute names to retrieve
            
        Returns:
            dict: dictionary representation of the student
        """
        pass
    
    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance
        
        Args:
            json (dict): dictionary with new attribute values
        """
        pass