import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    X=np.array(X)
    if X.ndim!=2:
        return None
    N,D=X.shape
    if N<2:
        return None
    X_mean=X-np.mean(X,axis=0)
    X_cov=(X_mean.T @ X_mean)/(N-1)
    return X_cov