def winsorize(values, lower_pct, upper_pct):
    sorted_values=sorted(values)
    n=len(sorted_values)
    def percentile(p):
        k=(n-1)*p/100
        lower=int(k)
        higher=min(int(k)+1,n-1)
        return sorted_values[lower]+(k-lower)*(sorted_values[higher]-sorted_values[lower])
    lower=percentile(lower_pct)
    upper=percentile(upper_pct)
    return [float(max(lower,min(upper,v)))for v in values]