import numpy as np

def pearson_correlation(X):
    X=np.array(X)
    if X.ndim!=2:
        return None
    N,D=X.shape
    if N<2:
        return None
    X_centered=X-np.mean(X,axis=0)
    X_cov=(X_centered.T @ X_centered)/(N-1)
    std_dev=np.std(X,axis=0,ddof=1)
    std_outer=np.outer(std_dev,std_dev)
    norm=X_cov/std_outer
    return norm