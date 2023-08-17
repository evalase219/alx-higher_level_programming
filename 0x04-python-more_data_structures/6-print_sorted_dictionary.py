#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Print a dictionary by ordered keys"""
    ord_keys = list(a_dictionary.keys())
    ord_keys.sort()
    for element in ord_keys:
        print("{}: {}".format(element, a_dictionary.get(element)))
