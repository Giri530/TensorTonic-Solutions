import numpy as np
def roc_curve(y_true, y_score):
    y_true = np.array(y_true,  dtype=float)
    y_score= np.array(y_score, dtype=float)
    sorted_index= np.argsort(y_score)[::-1]
    y_score_sorted= y_score[sorted_index]
    y_true_sorted= y_true[sorted_index]
    P = np.sum(y_true == 1)
    N = np.sum(y_true == 0)
    tprs = [0.0]
    fprs= [0.0]
    thresholds = [np.inf]
    tp= 0
    fp=0
    for i in range(len(y_score_sorted)):
        if y_true_sorted[i] == 1:
            tp += 1
        else:
            fp +=1
        if i + 1 < len(y_score_sorted) and y_score_sorted[i] == y_score_sorted[i+1]:
            continue
        tprs.append(tp / P)
        fprs.append(fp / N)
        thresholds.append(y_score_sorted[i])
    return np.array(fprs), np.array(tprs), np.array(thresholds)
