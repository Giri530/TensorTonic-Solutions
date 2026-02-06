import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    a=np.asarray(A)
    get_diagonal=np.diag(a)
    return sum(get_diagonal)
