#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to print x elements of a list.
# demonstrates how to use a try ... except for exception handling
#
# (C) 2024 Dejvid Papa, Tirana ,Albania
# email dejvidpapa@gmail.com
# ----------------------------------------------------------
def safe_print_list(my_list=[], x=0):
    num_of_elements = 0
    for index in range(x):
        try:
            print(my_list[index], end="")
            num_of_elements += 1
        except IndexError:
            break

    print()
    return num_of_elements-
