import numpy as np

def tanh(x):
    x=np.asarray(x)
    minus_exp=np.exp(x)-np.exp(-x)
    plus_exp=np.exp(x)+np.exp(-x)
    return minus_exp/plus_exp