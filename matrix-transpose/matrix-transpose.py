import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    matrix=np.asarray(A)
    matrix_transpose=np.transpose(matrix)
    return matrix_transpose
