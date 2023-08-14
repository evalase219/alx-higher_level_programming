#!/usr/bin/python3
#1-element_at.py

def element_at(my_list, idx):
    """Retrieve an element from a list"""

    if idx < 0:
        return None
    elif idx > (len(my_list) - 1):
        return None
    else:
        return (my_list[idx])
