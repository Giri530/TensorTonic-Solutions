import numpy as np

def matrix_trace(A):
    a=np.asarray(A,dtype=float)
    diag=np.diag(a)
    sum_diag=sum(diag)
    return sum_diag
