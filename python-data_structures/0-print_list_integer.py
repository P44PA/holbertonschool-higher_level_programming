#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if len(my_list) ==  0:
        return []
    elif len(my_list) == 1:
        return my_list
    else:
        for i in my_list:
            print("{}".format(i))
