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

def gen_F(seq):
    n = len(seq)
    f = np.zeros((n+1, n+1, n+1, n+1, n+1), dtype=int)      # f[m,j,i,k,l]
