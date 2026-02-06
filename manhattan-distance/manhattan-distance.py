import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x=np.asarray(x)
    y=np.asarray(y)
    manhattan_distance=np.linalg.norm(x-y,1)
    return manhattan_distance