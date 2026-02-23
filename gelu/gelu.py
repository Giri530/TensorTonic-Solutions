import numpy as np
import math
def erf_approx(x):
    a1, a2, a3, a4, a5 = 0.254829592, -0.284496736, 1.421413741, -1.453152027, 1.061405429
    p = 0.3275911
    sign = np.sign(x)
    x = np.abs(x)
    t = 1.0 / (1.0 + p * x)
    t_poly = t * (a1 + t * (a2 + t * (a3 + t * (a4 + t * a5))))
    y = 1.0 - t_poly * np.exp(-x * x)
    return sign * y

def gelu(x):
    x=np.asarray(x,dtype=float)
    return 0.5*x*(1+erf_approx(x/np.sqrt(2)))
