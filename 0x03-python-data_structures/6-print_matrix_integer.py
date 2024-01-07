#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if type(matrix) != list:
        return
    for row in matrix:
        if len(row) > 0:
            print('{:d}'.format(row[0]), end='')
            for num in row[1:]:
                print(' {:d}'.format(num), end='')
        print('')
