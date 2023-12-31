#!/usr/bin/python3

def safe_print_division(a, b):
    """Division of two integers"""
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
