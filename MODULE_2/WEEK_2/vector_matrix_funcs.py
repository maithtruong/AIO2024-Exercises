import numpy as np
import math


def compute_vector_length(vector):

    squared_sum = 0

    for element in vector:
        squared_sum += element**2

    len_of_vector = math.sqrt(squared_sum)

    return len_of_vector


def compute_dot_product(vector1, vector2):

    result = 0

    for i, j in zip(vector1, vector2):
        result += (i * j)

    return result


def matrix_multi_vector(matrix, vector):
    result = []
    for row in matrix:
        row_sum = 0
        for i, j in zip(row, vector):
            row_sum += i*j
        result.append(row_sum)
    return result


def matrix_multi_matrix(matrix1, matrix2):
    matrix_result = []
    for row_index in range(0, matrix1.shape[0]):
        row_result = []
        for col_index in range(0, matrix2.shape[1]):
            element = 0
            for i, j in zip(matrix1[row_index, :], matrix2[:, col_index]):
                element += i*j
            row_result.append(element)

        matrix_result.append(row_result)
    return matrix_result


def inverse_matrix(matrix):

    if matrix.shape != (2, 2):
        raise ValueError("Input must be a 2x2 matrix.")

    det = matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]

    if det == 0:
        return "Matrix not invertible."

    y = np.array([[matrix[1, 1], -matrix[0, 1]],
                  [-matrix[1, 0], matrix[0, 0]]])

    inv = 1 / det * y
    return inv
