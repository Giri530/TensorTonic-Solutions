import numpy as np

def poisson_pmf_cdf(lam, k):
    k=int(k)
    log_k_factorial=np.sum(np.log(np.arange(1,k+1)))
    log_pmf=-lam+k*np.log(lam)-log_k_factorial
    pmf=np.exp(log_pmf)
    i=np.arange(0,k+1)
    log_factorial=np.cumsum(np.concatenate([[0],np.log(np.arange(1,k+1))]))
    log_pmfs=-lam+i*np.log(lam)-log_factorial
    cdf=np.sum(np.exp(log_pmfs))
    return float(pmf),float(cdf)
                            