# DEFINE: 
# d(m, i, j, k, l) = f(m, i, j, k, l) - f(m, i-1, j, k, l)
# 
# Question: 
# Is it possible to get d(m, i, j, k, l) from d(m-1, i, j, k, l) and d(m, i, j, k-1, l)?
# 
# Thus:
# d(m-1, i, j, k, l) = f(m-1, i, j, k, l) - f(m-1, i-1, j, k, l)
# d(m, i, j, k-1, l) = f(m, i, j, k-1, l) - f(m, i-1, j, k-1, l)

import numpy as np

# gamma(m, x, seq) is the largest value of r such that r <= x and 
# seq[r] == seq[m], or 0 if no such value exists
def gamma(m, x, seq):
    for r in range(x, 0, -1):
        if seq[r-1] == seq[m-1]:
            return r
    return 0

def gen_D(seq):
    n = len(seq)
    f = np.zeros((n+1, n+1, n+1, n+1, n+1), dtype=int)      # f[m,j,i,k,l]
    d = np.zeros((n+1, n+1, n+1, n+1, n+1), dtype=int)      # d[m,j,i,k,l]

    for m in range(1, n+1):
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                for k in range(j, n+1):
                    for l in range(k+1, m+1):
                        f[m, j, i, k, l] = f[m - 1, j, i, k, l]
                        if gamma(m, i, seq) > 0 and gamma(m, k, seq) >= j:
                            f[m, j, i, k, l] = max(f[m, j, i, k, l], 
                                                   f[m-1, j, gamma(m, i, seq)-1, gamma(m, k, seq)-1, l]+1)
                        d[m, j, i, k, l] = f[m, j, i, k, l] - f[m, i-1, j, k, l]
    return d
    

