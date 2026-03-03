import numpy as np

def auc(fpr, tpr):
    fpr=np.asarray(fpr)
    tpr=np.asarray(tpr)
    sorted_index=np.argsort(fpr)
    fpr_sort=fpr[sorted_index]
    tpr_sort=tpr[sorted_index]
    width=fpr[1:]-fpr[:-1]
    height=tpr[1:]+tpr[:-1]
    auc=np.sum((width*height)/2)
    return float(auc)