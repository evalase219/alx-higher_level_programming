#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Print x elements of a list"""
    count = 0
    for element in range(x):
        try:
            print("{}".format(my_list[element]), end="")
            count += 1
        except Exception:
            break
    print("")
    return (count)
