import numpy as np
def positional_encoding(seq_len, d_model, base=10000.0):
    position = np.arange(seq_len, dtype=float)[:, np.newaxis]
    i = np.arange(d_model // 2, dtype=float)
    div = np.power(base, 2 * i / d_model)
    angle = position / div
    sin_angle = np.sin(angle)
    cos_angle = np.cos(angle)
    output_matrix = np.zeros((seq_len, d_model), dtype=float)
    output_matrix[:, 0::2][:, :sin_angle.shape[1]] = sin_angle
    output_matrix[:, 1::2][:, :cos_angle.shape[1]] = cos_angle
    if d_model % 2 == 1:
        last_dim = d_model - 1
        last_div = np.power(base, last_dim / d_model)
        output_matrix[:, -1] = np.sin(position / last_div).squeeze()
    return output_matrix