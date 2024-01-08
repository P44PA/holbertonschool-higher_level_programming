#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to print x elements of a list.
# demonstrates how to use a try ... except for exception handling
#
# (C) 2024 Dejvid Papa, Tirana ,Albania
# email dejvidpapa@gmail.com
# -----------------------------------------------------------
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    result = 0
    for index in range(0, list_length):
        try:
            result = my_list_1[index] / my_list_2[index]
        except TypeError:
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            pass
        new_list.append(result)
    return new_list
