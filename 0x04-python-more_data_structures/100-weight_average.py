#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    res = 0
    total_weight = 0
    for t in my_list:
        res += t[0] * t[1]
        total_weight += t[1]
    return res/total_weight
