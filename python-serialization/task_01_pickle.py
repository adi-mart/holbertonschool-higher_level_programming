#!/usr/bin/python3
"""Custom object with pickle serialization capabilities."""
import pickle


class CustomObject:
    """A custom class that can be serialized and deserialized using pickle."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance.

        Args:
            name (str): The name of the person
            age (int): The age of the person
            is_student (bool): Whether the person is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes in the specified format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance of the object to a file.

        Args:
            filename (str): The filename to save the serialized object to
        """
        if not isinstance(filename, str) or not filename:
            return None
        else:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file.

        Args:
            filename (str): The filename to load the serialized object from

        Returns:
            CustomObject or None: The deserialized object or None if error
        """
        if not isinstance(filename, str) or not filename:
            return None
        else:
            with open(filename, 'rb') as f:
                loaded_data = pickle.load(f)
            return (loaded_data)
