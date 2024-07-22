import numpy as np
import math
from vector_matrix_funcs import (
    compute_vector_length, 
    compute_dot_product, 
    matrix_multi_vector, 
    matrix_multi_matrix, 
    inverse_matrix
)
from cosine_similarity import compute_cosine
from eigen import compute_eigenvalues_eigenvectors

print('Question 1:')
vector = np.array([-2, 4, 9, 21])
result = compute_vector_length(vector)
print(round(result, 2))
# Expected: (d) 23.28

print('\nQuestion 2:')
v1 = np.array([0, 1, -1, 2])
v2 = np.array([2, 5, 1, 0])
result = compute_dot_product(v1, v2)
print(round(result, 2))
# Expected: (b) 4

print('\nQuestion 3:')
x = np.array([[1, 2],
              [3, 4]])
k = np.array([1, 2])
result = x.dot(k)
print('result \n', result)
# Expected: (a) [5 11]

print('\nQuestion 4:')
x = np.array([[-1, 2],
              [3, -4]])
k = np.array([1, 2])
result = x @ k
print('result \n', result)
# Expected: (a) [5 -5]

print('\nQuestion 5:')
m = np.array([[-1, 1, 1], [0, -4, 9]])
v = np.array([0, 2, 1])
result = matrix_multi_vector(m, v)
print(result)
# Expected: (d) [3 2]

print('\nQuestion 6:')
m1 = np.array([[0, 1, 2], [2, -3, 1]])
m2 = np.array([[1, -3], [6, 1], [0, -1]])
result = matrix_multi_matrix(m1, m2)
print(result)
# Expected: (a) [[9 -1], [-16 -10]]

print('\nQuestion 7:')
m1 = np.eye(3)
m2 = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
result = m1 @ m2
print(result)
# Expected: (a) [[1. 1. 1.], [2. 2. 2.], [3. 3. 3.]]

print('\nQuestion 8:')
m1 = np.eye(2)
m1 = np.reshape(m1, (-1, 4))[0]
m2 = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
result = m1 @ m2
print(result)
# Expected: (b) [4. 4. 4. 4.]

print('\nQuestion 9:')
m1 = np.array([[1, 2], [3, 4]])
m1 = np.reshape(m1, (-1, 4), "F")[0]
m2 = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
result = m1 @ m2
print(result)
# Expected: (a) [30 30 30 30]

print('\nQuestion 10:')
m1 = np.array([[-2, 6], [8, -4]])
result = inverse_matrix(m1)
print(result)
# Expected: (a) [[0.1 0.15], [0.2 0.05]]

print('\nQuestion 11:')
matrix = np.array([[0.9, 0.2], [0.1, 0.8]])
eigenvalues, eigenvectors = compute_eigenvalues_eigenvectors(matrix)
print(eigenvectors)
# Expected: (a) [[0.89442719 -0.70710678], [0.4472136 0.70710678]]

print('\nQuestion 12:')
x = np.array([1, 2, 3, 4])
y = np.array([1, 0, 3, 0])
result = compute_cosine(x, y)
print(round(result, 3))
# Expected: (c) 0.577
