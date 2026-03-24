import numpy as np

def chi2_independence(C):
    C=np.array(C,dtype=float)
    r_total=C.sum(axis=1,keepdims=True)
    c_total=C.sum(axis=0,keepdims=True)
    total=C.sum()
    expected=(r_total@c_total)/total
    chi_square=np.sum((C-expected)**2/expected)
    return float(chi_square),expected