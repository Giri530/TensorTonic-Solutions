import numpy as np

def percentiles(x, q):
    x=np.sort(x)
    n=len(x)
    q=np.array(q)/100.0
    index=(n-1)*q
    lower_index=np.floor(index).astype(int)
    higher_index=np.ceil(index).astype(int)
    delta=index-lower_index
    lower_value=x[lower_index]
    higher_value=x[higher_index]
    return lower_value+(higher_value-lower_value)*delta
    