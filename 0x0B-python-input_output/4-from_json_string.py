#!/usr/bin/python3
"""Define string from JSON function."""
import json


def from_json_string(my_str):
    """Return an object representation from JSON string.

    Arg:
        my_str (str): The string to return.
    """
    return json.loads(my_str)
