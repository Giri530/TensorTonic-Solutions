import numpy as np
def matrix_normalization(matrix, axis=None, norm_type='l2'):
    matrix = np.asarray(matrix, dtype=float)
    if matrix.ndim != 2:
        return None
    norm_map = {
        'l1': 1,
        'l2': 2,
        'max': np.inf
    }
    if norm_type not in norm_map:
        return None
    ord_val = norm_map[norm_type]
    if axis is None:
        if norm_type == 'l2':
            norm = np.sqrt(np.sum(matrix ** 2))
        elif norm_type == 'l1':
            norm = np.sum(np.abs(matrix))
        else:  # 'max'
            norm = np.max(np.abs(matrix))
        
        # Avoid div by zero
        if norm == 0:
            norm = 1.0
        return matrix / norm
    
    # Axis-specific normalization
    # Validate axis value before calling np.linalg.norm
    if not isinstance(axis, (int, type(None))):
        return None
    
    if axis < -matrix.ndim or axis >= matrix.ndim:
        return None
    
    # Now safe to compute
    try:
        norms = np.linalg.norm(matrix, ord=ord_val, axis=axis, keepdims=True)
    except np.AxisError:
        return None
    
    # Replace zero norms with 1 to avoid div-by-zero
    norms = np.where(norms == 0, 1.0, norms)
    
    return matrix / norms