#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to print x elements of a list.
# demonstrates how to use a try ... except for exception handling
#
# (C) 2024 Dejvid Papa, Tirana ,Albania
# email dejvidpapa@gmail.com
# -----------------------------------------------------------
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += (a ** b) / i
        except Exception:
            result = a + b
            break
    return result
