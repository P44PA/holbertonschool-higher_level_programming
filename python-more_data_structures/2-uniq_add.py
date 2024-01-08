#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqueList = []
    for i in my_list:
        if i not in uniqueList:
            uniqueList.append(i)
    return sum(uniqueList)
