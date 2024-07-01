# DEFINE: 
# d(m, i, j, k, l) = f(m, i, j, k, l) - f(m, i-1, j, k, l)
# 
# Question: 
# Is it possible to get d(m, i, j, k, l) from d(m-1, i, j, k, l) and d(m, i, j, k-1, l)?
# 
# Thus:
# d(m-1, i, j, k, l) = f(m-1, i, j, k, l) - f(m-1, i-1, j, k, l)
# d(m, i, j, k-1, l) = f(m, i, j, k-1, l) - f(m, i-1, j, k-1, l)

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
import sys
import random

# gamma(m, x, seq) is the largest value of r such that r <= x and 
# seq[r] == seq[m], or 0 if no such value exists
def gamma(m, x, seq):
    for r in range(x, 0, -1):
        if seq[r-1] == seq[m-1]:
            return r
    return 0

def gen_D(seq, count, num_k, num_m):
    n = len(seq)
    f = np.zeros((n+1, n+1, n+1, n+1, n+1), dtype=int)      # f[m,j,i,k,l]
    d = np.zeros((n+1, n+1, n+1, n+1, n+1), dtype=int)      # d[m,j,i,k,l]

    for m in range(1, n+1):
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                for k in range(j, n+1):
                    for l in range(k+1, m+1):
                        f[m, i, j, k, l] = f[m-1, i, j, k, l]
                        if gamma(m, i, seq) > 0 and gamma(m, k, seq) >= j:
                            f[m, i, j, k, l] = max(f[m, i, j, k, l], 
                                                   f[m-1, gamma(m, i, seq)-1, j, gamma(m, k, seq)-1, l]+1)
                        d[m, i, j, k, l] = f[m, i, j, k, l] - f[m, i-1, j, k, l]
                        
                      # Test page 2 - 7/01 
                        if seq[k-1] != seq[m-1]:
                          if seq[i-1] == seq[k-1]: 
                            #print(f" sk = {seq[k-1]} != sm={seq[m-1]}, and sk= si={seq[i-1]}") 
                            if d[m, i, j, k, l] ==  d[m-1, i, j, k, l]:
                              num_k = num_k + 1
                             # print(f"k-case:  d[m, i, j, k, l] = { d[m, i, j, k, l]},  d[m, i, j, k-1, l] = { d[m-1, i, j, k-1, l]}")
                            if d[m, i, j, k, l] ==  d[m, i, j, k-1, l]:
                              num_m = num_m + 1
                              #print(f"m-case:  d[m, i, j, k, l] = { d[m, i, j, k, l]},  d[m-1, i, j, k, l] = { d[m-1, i, j, k, l]}")
                             #print(f"neither:  d[m, i, j, k, l] = { d[m, i, j, k, l]},  d[m-1, i, j, k, l] = { d[m-1, i, j, k, l]},  d[m, i, j, k-1, l] = { d[m, i, j, k-1, l]}")

    # if count % 1000 == 0:
    #     print(f"PASSED. {count}")
    print(num_k, num_m)
    return num_k, num_m

# characters allowed in test string 
alphabet = ['a', 'b', 'c', 'd', 'e']

# max size of the test string 
max_length = 20

# number of test cases
num_tests = 200

# Counts the number of k and m 
num_k = 0
num_m = 0

for x in range(num_tests):
    seq = ""
    for _ in range(random.randint(max_length-5, max_length)):      
        seq += str(random.choice(alphabet))
    num_k2, num_m2 = gen_D(seq, x, num_k, num_m)
# print(f"{num_k} k-cases, {num_m} m-cases")
