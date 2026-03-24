import numpy as np

def expected_value_discrete(x, p):
    if not np.isclose(np.sum(p), 1, atol=1e-6):
        raise ValueError("Probabilities must sum to 1")
    return float(np.sum(np.array(x)*np.array(p)))