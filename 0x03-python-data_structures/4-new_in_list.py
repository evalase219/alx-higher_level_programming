#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace an element in a list at a specific position
    without modifying the original list"""
    temp_list = my_list[:]
    if 0 <= idx < len(my_list):
        temp_list[idx] = element
        return(temp_list)
    return(my_list)
