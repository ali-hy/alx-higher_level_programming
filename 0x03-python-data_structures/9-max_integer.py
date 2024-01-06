#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return
    res = my_list[0]
    for i in my_list[1:]:
        if i > res:
            res = i
    return res
