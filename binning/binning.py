def binning(values, num_bins):
    min_val=min(values)
    max_val=max(values)
    width=(max_val-min_val)/num_bins
    if min_val==max_val:
        return[0]*len(values)
    return[min(int((val-min_val)/width),num_bins-1)for val in values]
    