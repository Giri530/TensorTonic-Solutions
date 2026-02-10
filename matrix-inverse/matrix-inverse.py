import numpy as np

def matrix_inverse(A):
    A=np.asarray(A,dtype=float)
    if A.ndim!=2:
        return None
    rows,col=A.shape
    if rows!=col or rows==0:
        return None
    try:
        A_inv = np.linalg.inv(A)
        error = np.linalg.norm(A @ A_inv - np.eye(rows))
        if error >= 1e-7:
            return None
        return A_inv
    except np.linalg.LinAlgError:
        return None
