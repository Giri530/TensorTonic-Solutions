import numpy as np
def jaccard_similarity(set_a, set_b):
    if not set_a and not set_b:
        return 0.0
    set_a=np.asarray(set_a)
    set_b=np.asarray(set_b)
    intersection=np.intersect1d(set_a,set_b)
    union=np.union1d(set_a,set_b)
    size_inter=np.size(intersection)
    size_union=np.size(union)
    return float(size_inter/size_union)