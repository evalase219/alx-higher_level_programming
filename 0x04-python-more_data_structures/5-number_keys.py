#!/usr/bin/python3
def number_keys(a_dictionary):
    """Return the number of keys in a dictionary"""
    num = 0
    list_keys = list(a_dictionary.keys())
    for element in list_keys:
        num += 1
    return (num)
