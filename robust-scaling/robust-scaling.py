def robust_scaling(values):
    def median(lst):
        n=len(lst)
        s=sorted(lst)
        if n % 2 == 1:
            return float(s[n // 2])
        else:
            return (s[n // 2 - 1] + s[n // 2]) / 2.0
    n = len(values)
    s = sorted(values)
    if n == 1:
        return [0.0]
    med = median(s)
    lower = s[:n // 2]
    upper = s[n - n // 2:]
    Q1 = median(lower)
    Q3 = median(upper)
    IQR = Q3 - Q1
    if IQR == 0:
        return [float(x - med) for x in values]

    return [float((x - med) / IQR) for x in values]