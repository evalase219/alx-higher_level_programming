#!/usr/bin/python3
"""A module for square with private attribute"""

class Square:
    """Defines a square"""

    def __init__(self, size):
        """
        This method constructs a square with size variable
        Args:
            size: equal length of a square
        """

        self.__size = size
