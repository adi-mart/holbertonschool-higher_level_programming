#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for number in matrix:
        new_number = []
        for i in number:
            new_number.append(i ** 2)
        new_matrix.append(new_number)
    return (new_matrix)
