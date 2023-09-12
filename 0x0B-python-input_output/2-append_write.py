#!/usr/bin/python3
"""Define a text file appending function."""


def append_write(filename="", text=""):
    """Append a string to the end of UTF8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Return:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
