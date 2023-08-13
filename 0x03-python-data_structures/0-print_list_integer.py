#!/usr/bin/python3
#0-print_list_integer.py


def print_list_integer(my_list=[]):
    """Print all integers of a list"""

    elements = 0
    while elements < len(my_list):
        print("{:d}".format(my_list[elements]))
        elements += 1 
