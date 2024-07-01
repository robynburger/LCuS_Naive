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
                        
                        # test 07/01 - 1.2 forward
                        if seq[m-1] == seq[k-1] and d[m-1, i, j, k-1, l] == 0 and d[m, i, j, k, l] == 1:
                            if seq[k-1] != seq[i-1]:
                                sys.exit(f"ERROR: s_k != s_i {seq}. i: {i}, j: {j}, k: {k}, l: {l}, m: {m}")
                            exists_1 = False
                            for r in range(gamma(k, i-1, seq), i):
                                if r == 0 or d[m-1, r, j, k-1, l] == 1:
                                    exists_1 = True
                            if exists_1 == False:
                                sys.exit(f"ERROR: {seq}. i: {i}, j: {j}, k: {k}, l: {l}, m: {m}")


                        """
                        # test 07/01 - 1.1 reverse
                        if seq[m-1] == seq[k-1] and d[m-1, i, j, k-1, l] == 1:
                            all_zero = True
                            for r in range(gamma(k, i-1, seq), i):
                                if r == 0 or d[m-1, r, j, k-1, l] != 0:
                                    all_zero = False
                            if all_zero and d[m, i, j, k, l] != 0:
                                sys.exit(f"ERROR: {seq}. i: {i}, j: {j}, k: {k}, l: {l}, m: {m}")
        
                        # test 07/01 - 1.1 forward
                        if seq[m-1] == seq[k-1] and d[m-1, i, j, k-1, l] == 1 and d[m, i, j, k, l] == 0:
                            for r in range(gamma(k, i-1, seq), i):
                                if r == 0 or d[m-1, r, j, k-1, l] != 0:
                                    print(f"r: {r}")
                                    sys.exit(f"ERROR: {seq}. i: {i}, j: {j}, k: {k}, l: {l}, m: {m}")
                        """
                                    
                        """
                        print(f"d[{m}, {i}, {j}, {k}, {l}] = {d[m, i, j, k, l]}")
                        print(f"d[{m-1}, {i}, {j}, {k}, {l}] = {d[m-1, i, j, k, l]}")
                        if k-1 >= j:
                            print(f"d[{m}, {i}, {j}, {k-1}, {l}] = {d[m, i, j, k-1, l]}")
                        for r in range(gamma(m, i-1, seq), i):
                            print(f"    m-1 case:")
                            print(f"    d[{m-1}, {r}, {j}, {k}, {l}] = {d[m-1, r, j, k, l]}")
                            if k-1 >= j:
                                print(f"    k-1 case:")
                                print(f"    d[{m}, {r}, {j}, {k-1}, {l}] = {d[m, r, j, k-1, l]}")
                            if d[m-1, r, j, k, l] == 1 or d[m, r, j, k-1, l] == 1:
                                sys.exit("ERROR: d = 1, should be 0.")
                        print(f"    s[i] = {seq[i-1]}, s[k] = {seq[k-1]}, s[m] = {seq[m-1]}")
                        print("\n")
                        """
    if count % 1000 == 0:
        print(f"PASSED. {count}")

# characters allowed in test string 
alphabet = ['a', 'b', 'c', 'd', 'e']

# max size of the test string 
max_length = 20

# number of test cases
num_tests = 20000

for x in range(num_tests):
    seq = ""
    for _ in range(random.randint(max_length-5, max_length)):      
        seq += str(random.choice(alphabet))
    gen_D(seq, x)