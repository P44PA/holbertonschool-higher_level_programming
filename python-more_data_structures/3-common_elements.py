#!/usr/bin/python3
def common_elements(set_1, set_2):
    not_unique = []
    for i in set_1:
        if i in set_2:
            not_unique.append(i)
    return set(not_unique)
