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

def gen_D(seq, count):
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
        
                        if seq[i-1] == seq[k-1] == seq[m-1]:
                            # print(f"d[{m}, {i}, {j}, {k}, {l}] = {d[m, i, j, k, l]}")
                            # print(f"d[{m-1}, {i}, {j}, {k}, {l}] = {d[m-1, i, j, k, l]}")
                            # if k-1 >= j:
                            #     print(f"d[{m}, {i}, {j}, {k-1}, {l}] = {d[m, i, j, k-1, l]}")
                            if d[m-1, i, j, k-1, l] == 0:
                                if d[m, i, j, k, l] == 1:
                                    err = True
                                    print(seq)
                                    for r in range(gamma(m, i-1, seq), i):
                                        print(r)
                                    print("\n")
                                    for r in range(gamma(m, i-1, seq), i):
                                        print(f"d[{m-1}, {r+1}, {j}, {k-1}, {l}] = {d[m-1, r+1, j, k-1, l]}")
                                        if k-1 >= j:
                                            print(f"d[{m-1}, {r}, {j}, {k-1}, {l}] = {d[m-1, r, j, k-1, l]}")
                                            if d[m-1, r, j, k-1, l] == 1:
                                                err = False
                                    if err:
                                        sys.exit("Error")
                                            # elif d[m-1, r, j, k-1, l] == 0:
                                                #print(f"    s[i] = {seq[i-1]}, s[k] = {seq[k-1]}, s[m] = {seq[m-1]}")
                                                       # print("\n")
    # if count % 100 == 0:
    print(f"Passed {count}")

# characters allowed in test string 
alphabet = ['a', 'b', 'c', 'd']

# max size of the test string 
max_length = 5

# number of test cases
num_tests = 1000

# for x in range(num_tests):
#     seq = ""
#     for _ in range(random.randint(max_length-5, max_length)):
#       seq += str(random.choice(alphabet))
#     gen_D(seq, x )
    
gen_D("aaa", 1)