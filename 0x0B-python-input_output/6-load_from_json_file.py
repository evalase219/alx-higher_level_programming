#!/usr/bin/python3
"""Define creaate object from JSON file function."""
import json


def load_from_json_file(filename):
    """Create an object from a JSON file.

    Arg:
        filename (str): The name of the object to create.
    """
    with open(filename) as f:
        return json.load(f)
