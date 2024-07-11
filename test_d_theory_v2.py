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
                        
                      # test theory 7/08
                        if seq[k-1] != seq[m-1]:
                            if d[m, i, j, k-1, l] != d[m-1, i, j, k, l]:
                                d_sum_k = 0
                                d_sum_m = 0
                                for prev_i in range(1, i+1):
                                    d_sum_k += d[m, prev_i, j, k-1, l]
                                    d_sum_m += d[m-1, prev_i, j, k, l]
                                test_d = 0
                                if d_sum_m > d_sum_k:
                                    test_d = d[m-1, i, j, k, l]
                                elif d_sum_k > d_sum_m:
                                    test_d = d[m, i, j, k-1, l]
                                else:
                                    test_d = 0
                                if d[m, i, j, k, l] != test_d:
                                    print(f"d[m, i, j, k, l] = { d[m, i, j, k, l]},  d[m, i, j, k-1, l] = { d[m, i, j, k-1, l]}")
                                    print(f"gamma(m, k, seq) = {gamma(m, k, seq)}")
                                    print(f"k = {k}")
                                    print(f"gamma(m-1, k, seq) = {gamma(m-1, k, seq)}")
                                    sys.exit("ERROR!")
                        
                            
                            #print(f" sk = {seq[k-1]} != sm={seq[m-1]}, and sk= si={seq[i-1]}") 
                            # if d[m, i, j, k, l] ==  d[m-1, i, j, k, l]:
                            #   num_k = num_k + 1
                            #   if d[m, i, j, k, l] == 0:
                            #     print(f"m-case:  d[m, i, j, k, l] = { d[m, i, j, k, l]},  d[m-1, i, j, k, l] = { d[m-1, i, j, k, l]}")
                            # num_m = num_m + 1
                              # if  d[m, i, j, k, l] == 0:
                            if gamma(m, k-1, seq) < 1:  
                            if d[m, i, j, k, l] ==  d[m-1, i, j, k, l]:
                              count == count + 1
                            else:
                                  print(f"d[m, i, j, k, l] = { d[m, i, j, k, l]},  d[m, i, j, k-1, l] = { d[m, i, j, k-1, l]}")
                                  print(f"gamma(m, k, seq) = {gamma(m, k, seq)}")
                                  print(f"k = {k}")
                                  print(f"gamma(m-1, k, seq) = {gamma(m-1, k, seq)}")
                                  sys.exit("ERROR!")
                                  
                               

                             #print(f"neither:  d[m, i, j, k, l] = { d[m, i, j, k, l]},  d[m-1, i, j, k, l] = { d[m-1, i, j, k, l]},  d[m, i, j, k-1, l] = { d[m, i, j, k-1, l]}")
                            

    if count % 1000 == 0:
        print(f"PASSED. {count}")

# characters allowed in test string 
alphabet = ['a', 'b', 'c', 'd', 'e']

# max size of the test string 
max_length = 20

# number of test cases
num_tests = 100000

# Counts the number of k and m 
# num_k = 0
# num_m = 0

for x in range(num_tests):
    seq = ""
    for _ in range(random.randint(max_length-5, max_length)):      
        seq += str(random.choice(alphabet))
    gen_D(seq, x)
# print(f"{num_k} k-cases, {num_m} m-cases")
