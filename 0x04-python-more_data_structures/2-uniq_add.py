#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Add all unique integers in a list"""
    uniq_integer = set(my_list)
    num = 0
    for elements in uniq_integer:
        num += elements
    return (num)
