import numpy as np

def auc(fpr, tpr):
    fpr=np.asarray(fpr)
    tpr=np.asarray(tpr)
    sorted_index=np.argsort(fpr)
    fpr_Sort=fpr[sorted_index]
    tpr_sort=tpr[sorted_index]
    width=fpr_Sort[1:]-fpr_Sort[:-1]
    height=tpr_sort[1:]+tpr_sort[:-1]
    auc=np.sum(width*height)/2
    return float(auc)