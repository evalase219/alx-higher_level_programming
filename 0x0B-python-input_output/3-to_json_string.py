#!/usr/bin/python3
"""Define a string to JSON function."""
import json


def to_json_string(my_obj):
    """Return the json representation of an object (string).

    Arg:
        my_obj (str): The object to return.
    """
    return json.dumps(my_obj)
