#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialization of a new square.
        Args:
            size(int): equal length of a square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size
