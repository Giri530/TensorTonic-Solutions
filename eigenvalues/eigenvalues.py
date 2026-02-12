import numpy as np
def calculate_eigenvalues(matrix):
    try:
        A = np.array(matrix, dtype=float)
    except (ValueError, TypeError):
        return None
    if A.ndim != 2 or A.shape[0] != A.shape[1] or A.shape[0] == 0:
        return None
    vals = np.linalg.eigvals(A)
    return vals[np.lexsort((vals.imag, vals.real))]