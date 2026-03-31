def min_max_scaling(data):
    if not data or not data[0]:
        return data
    num_rows=len(data)
    num_col=len(data[0])
    result=[[0.0] * num_col for _ in range(num_rows)]
    for i in range(num_col):
        col_values=[data[j][i] for j in range(num_rows)]
        col_min=min(col_values)
        col_max=max(col_values)
        col_range=col_max - col_min
        for j in range(num_rows):
            if col_range == 0:
                result[j][i] = 0.0
            else:
                result[j][i]=(data[j][i] - col_min) / col_range
    return result