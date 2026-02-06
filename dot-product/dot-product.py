import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    # Write code here
    x=np.asarray(x)
    y=np.asarray(y)
    if len(x)!=len(y):
        raise ValueError("Enter correct length:got{len(x)} and {{len(y)}")
    return float(np.dot(x,y))