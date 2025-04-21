#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print(end="$")
        print()
        
print_matrix_integer([[1, 2, 3], [4, 5, 6], [7, 8, 9]])