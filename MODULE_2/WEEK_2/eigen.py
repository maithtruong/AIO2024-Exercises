import numpy as np


def compute_eigenvalues_eigenvectors(matrix):

    if matrix.shape != (2, 2):
        raise ValueError("Input must be a 2x2 matrix.")

    a, b, c, d = matrix[0, 0], matrix[0, 1], matrix[1, 0], matrix[1, 1]

    trace = a + d
    determinant = a * d - b * c

    discriminant = trace**2 - 4 * determinant
    if discriminant < 0:
        raise ValueError("Eigenvalues are complex.")

    lambda1 = (trace + np.sqrt(discriminant)) / 2
    lambda2 = (trace - np.sqrt(discriminant)) / 2

    eigenvalues = (lambda1, lambda2)

    eigenvectors = []
    for eigenvalue in eigenvalues:

        A_minus_lambdaI = matrix - eigenvalue * np.eye(2)

        _, _, vh = np.linalg.svd(A_minus_lambdaI)
        eigenvector = vh[-1]
        eigenvectors.append(eigenvector)

    eigenvectors = np.column_stack(eigenvectors)

    return eigenvalues, eigenvectors
