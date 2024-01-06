#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) > 0:
            print('{}'.format(row[0]), end='')
            for num in row[1:]:
                print(' {}'.format(num), end='')
        print('')
