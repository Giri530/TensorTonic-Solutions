import numpy as np
from collections import Counter

def mean_median_mode(x):
    x=np.asarray(x)
    mean=np.mean(x)
    median=np.median(x)
    values,count=np.unique(x,return_counts=True)
    mode=float(values[np.argmax(count)])
    return mean,median,mode