import numpy as np

def t_test_one_sample(x, mu0):
    x=np.array(x)
    x_mean=np.mean(x)
    ssd=np.std(x,ddof=1)##ddof=1 is used for sample standard deviation,ddof=0 means used for population standard deviation
    n=len(x)
    t_test=(x_mean-mu0)/(ssd/np.sqrt(n))
    return float((t_test))
    