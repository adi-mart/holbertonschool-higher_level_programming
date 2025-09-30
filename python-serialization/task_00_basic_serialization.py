#!/usr/bin/python3
"""Basic serialization module for JSON operations."""
import pickle


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to a JSON file.

    Args:
        data: A Python Dictionary with data
        filename: The filename of the output JSON file
    """
    with open(filename, 'wb') as f:
        pickle.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize data from a JSON file.

    Args:
        filename: The filename of the input JSON file

    Returns:
        A Python Dictionary with the deserialized JSON data from the file
    """
    with open(filename, 'rb') as f:
        loaded_data = pickle.load(f)
    return (loaded_data)
