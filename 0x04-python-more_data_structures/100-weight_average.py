#!/usr/bin/python3
def weight_average(my_list=[]):
    res = 0
    total_weight = 0
    for t in my_list:
        res += t[0] * t[1]
        total_weight += t[1]
    return res/total_weight

my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))
