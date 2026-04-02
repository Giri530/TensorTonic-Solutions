def frequency_encoding(values):
    n=len(values)
    count={}
    for val in values:
        count[val]=count.get(val,0)+1
    return [count[val]/n for val in values]