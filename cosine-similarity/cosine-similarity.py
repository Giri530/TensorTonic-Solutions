import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    
    x=np.asarray(a)
    y=np.asarray(b)
    dot=np.dot(x,y)
    norm_a=np.linalg.norm(a)
    norm_b=np.linalg.norm(b)
    magnitude=norm_a*norm_b
    if norm_a==0 or norm_b==0:
        return 0
    return float(dot/magnitude)