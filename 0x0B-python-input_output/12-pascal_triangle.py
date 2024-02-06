#!/usr/bin/python3
'''pascal triangle'''


def pascal_triangle(n):
    '''returns list representing pascal's triangle at level n'''
    if (n <= 0):
        return []

    res = [1]
    n -= 1

    while n > 0:
        new_res = list(res)
        for i in range(1, len(new_res)):
            new_res[i] = res[i] + res[i-1]
        new_res.append(1)
        res = new_res
        n -= 1

    return res
