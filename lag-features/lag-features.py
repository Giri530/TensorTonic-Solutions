def lag_features(series, lags):
    result=[]
    max_lag=max(lags)
    for t in range(max_lag,len(series)):
        result.append([series[t-lag] for lag in lags])
    return result