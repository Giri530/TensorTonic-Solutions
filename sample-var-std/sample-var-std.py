import numpy as np

def sample_var_std(x):
    x=np.asarray(x,dtype=float)
    std=np.std(x,ddof=1)
    var=np.var(x,ddof=1)
    return float(var),float(std)