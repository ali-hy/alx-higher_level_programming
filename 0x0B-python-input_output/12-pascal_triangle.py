#!/usr/bin/python3
'''pascal triangle'''


def pascal_triangle(n):
    '''returns list representing pascal's triangle at level n'''
    if (n <= 0):
        return []

    res = [[1]]
    n -= 1

    while n > 0:
        new_level = list(res[-1])
        for i in range(1, len(new_level)):
            new_level[i] = res[-1][i] + res[-1][i-1]
        new_level.append(1)
        res.append(new_level)
        n -= 1

    return res


if __name__ == '__main__':
    print(pascal_triangle(5))
