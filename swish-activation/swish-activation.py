import numpy as np

def swish(x):
    x=np.asarray(x,dtype=float)
    return x*1/(1+np.exp(-x))