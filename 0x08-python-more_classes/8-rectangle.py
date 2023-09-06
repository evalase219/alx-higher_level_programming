#!/usr/bin/python3
"""Define a rectangle"""


class Rectangle:
    """Represent the area and perimeter of a rectangle.

    Attributs:
    number_of_instances (int): The number of the rectangle instances.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        Raises:
            TypeError: if the width or the height is not an integer.
            ValueError: if the width or the height is less than zero.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @classmethod
    def printed_symbol(cls):
        cls.print_symbol = print_symbol

    @property
    def width(self):
        """Get/set the current width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the current width of the rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the current area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the current perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Print the diagram of a rectangle with # character"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        for i in range(self.__height):
            print("{}".format(self.print_symbol) * self.__width, end=""
                    if i == (self.__height - 1) else "\n")
        return ""

    def __repr__(self):
        """Return a string representation of the rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletion of the rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.
            Raise:
                TypeError: if rect_1 or rect_2 is not an instance of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() == rect_2.area():
            return rect_1
        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2
