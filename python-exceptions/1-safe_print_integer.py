#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to print x elements of a list.
# demonstrates how to use a try ... except for exception handling
#
# (C) 2024 Dejvid Papa, Tirana ,Albania
# email dejvidpapa@gmail.com
# ----------------------------------------------------------
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        return False

    return True
