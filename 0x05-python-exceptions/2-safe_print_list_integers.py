#!/usr/bin/python3 

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x element of a list and only integers"""
    count = 0
    for element in range(0, x):
        try:
            print("{:d}".format(my_list[element]), end="")
            count += 1
        except (TypeError, ValueError):
            continue
    print("")
    return (count)
