#!/usr/bin/python3
"""Define a JSON file writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation.

    Args:
        my_obj (str): The string to write to
        filename (str): The name of the text file
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
