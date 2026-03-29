import numpy as np
def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
    x=np.asarray(x, dtype=float)
    N=len(x)
    if rng is not None:
        indices=rng.integers(0, N, size=(n_bootstrap, N))
    else:
        indices=np.random.randint(0, N, size=(n_bootstrap, N))
    boot_means=x[indices].mean(axis=1)
    alpha=1-ci
    lower=float(np.quantile(boot_means, alpha / 2))
    upper=float(np.quantile(boot_means, 1 - alpha / 2))
    return boot_means, lower, upper