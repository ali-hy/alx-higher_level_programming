#!/usr/bin/python3
def uniq_add(my_list=[]):
    added = set()
    res = 0
    for i in my_list:
        if i in added:
            continue
        res += i
        added.add(i)
    return res
