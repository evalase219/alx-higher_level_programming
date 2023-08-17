#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replace the occurrences of an element by another in a list"""
    new_list = list(map(lambda n: replace if n == search else n, my_list))
    return(new_list)
