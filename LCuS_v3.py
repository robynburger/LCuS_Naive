# version of LCuS with 6/27 change re: test_contiguous_j.py

import random
import numpy as np

# gamma(m, x, seq) is the largest value of r such that r <= x and 
# seq[r] == seq[m], or 0 if no such value exists

# characters allowed in test string 
alphabet = ['a', 'b', 'c']

# max size of the test string 
max_length = 15

# number of test cases
num_tests = 1000000000

def gamma(m, x, seq):
    for r in range(x, 0, -1):
        if seq[r-1] == seq[m-1]:
            return r
    return 0


def LCuS(seq):
    n = len(seq)
    f = np.zeros((n+1, n+1, n+1, n+1, n+1), dtype=int)      # f[m,j,i,k,l]
    b = np.zeros((n+1, n+1, n+1, n+1), dtype=int)

    for l in range(3, n+1):
        print(f"l = {l}")
        for k in range(2, l):
            print(f"k = {k}")
            for i in range(1, k):
                print(f"i = {i}")
                # Populate j vector for given i,k,l
                for j in range(i+1, k+1):
                    print(f"j = {j}")
                    f[n, j, i, k, l] = f[n - 1, j, i, k, l]
                    if gamma(n, i, seq) > 0 and gamma(n, k, seq) >= j:
                        f[n, j, i, k, l] = max(f[n, j, i, k, l], f[n-1, j, gamma(n, i, seq)-1, gamma(n, k, seq)-1, l]+1)
                    b[i, j, k, l] = f[n, j, i, k, l] - f[n, j, i-1, k, l]       
                    print(f"b[{i}, {j}, {k}, {l}] = {b[i, j, k, l]}") 
    # print(str(b))

    for p in range(1, n + 1): 
            print(f"p = {p}")
            for q in range(p+1, n):  
                print(f"q = {q}")
                score = 0;
                for j in range(2, n-q):
                    print(f"l = {l}")
                    print(f"b[{j-1}, {j}, {q}, {q+1}] = {b[j-1, j, q, q+1]}")
                    print(f"p={p}")
                    if b[j-1, j, q, q+1] >= p:
                        score += score + 1
                print(f"score[{p}, {q}] = {score}\n")
  

LCuS("aaa")

    # for q in range(2, n):
    #   for in range(p+1, n):  
    #     print(f"q = {q}")
    #     score = 0;

    #     for l in range(1, n + 1): 
    #         print(f"l = {l}")
    #         if a[n, p+1, l-1 + p, l] >= q + 1:
        #       score += score + 1
        #       print(f"score[{p}, {q}] = {score}\n")


            
