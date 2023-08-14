#!/usr/bin/python3
#2-replace_in_list.py


def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific position"""

    if my_list is None:
        return
    elif idx >= 0 and idx < len(my_list):
        my_list[idx] = element
        return(my_list)
