#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) > 0:
            print('{}'.format(row[0]), end='')
            for num in row[1:]:
                print(' {}'.format(num), end='')
        print('')


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix_integer(matrix)
print("--")
print_matrix_integer()
