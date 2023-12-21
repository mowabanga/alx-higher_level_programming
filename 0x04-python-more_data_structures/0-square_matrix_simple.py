#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix

    Args:
        matrix (list, optional): matrix. Defaults to [].
    """
    
    new_matrix = matrix[:]
    squared_matrix = [[x**2 for x in row] for row in matrix]
    return squared_matrix
        
square_matrix_simple([[1, 2, 3], [4, 5, 6], [7, 8, 9]])