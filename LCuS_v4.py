"""
First draft of algorithm updated as of 7/8
"""

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
    D = np.zeros((n+1, n+1, n+1, n+1), dtype=int)

# Populate D tensor 
    for i in range(1, n+1):
      for j in range(i+1, n+1):
        for k in range(j, n+1):
          for m in range(k+1, n+1):
                # sm = sk 
                if seq[m-1]==seq[k-1]:
                  # Case 1
                  if D[i, j, k-1, m-1] == 1:
                    for r in range(gamma(m, i-1, seq), i): 
                        if D[r, j, k-1, m-1] == 1:
                          D[i, j, k, m] == 0
                          break
                        D[i, j, k, m] == 1
                  # Case 2
                  if D[i, j, k-1, m-1] == 0:
                     if seq[i-1] == seq[k-1]:
                      for r in range(gamma(m, i-1, seq), i): 
                        if D[r, j, k-1, m-1] == 1:
                          D[i, j, k, m] == 1
                          break
                        D[i, j, k, m] == 0
                      else:
                         D[i, j, k, m] == 0
                  # sm != sk
                  else:
                    # Case 3:
                    if d[m, i, j, k-1, l] == d[m-1, i, j, k, l]:
                      D[i, j, k, m] == d[m, i, j, k-1, l]
                    # Case 4: (New case)
                    else:
                      d_sum_k = 0
                      d_sum_m = 0
                      for prev_i in range(1, i+1):
                          d_sum_k += d[m, prev_i, j, k-1, l]
                          d_sum_m += d[m-1, prev_i, j, k, l]
                      if d_sum_m > d_sum_k:
                          D[i, j, k, m] = d[m-1, i, j, k, l]
                      elif d_sum_k > d_sum_m:
                          D[i, j, k, m] = d[m, i, j, k-1, l]
                      else:
                          D[i, j, k, m] = 0
          print(f"i ={i}, j= {j}, k= {k}, m = {m}")
          print(str(D))
    # for p in range(1, n + 1): 
    #         print(f"p = {p}")
    #         for q in range(p+1, n):  
    #             print(f"q = {q}")
    #             score = 0;
    #             for j in range(2, n-q):
    #                 # print(f"l = {l}")
    #                 # print(f"b[{j-1}, {j}, {q}, {q+1}] = {b[j-1, j, q, q+1]}")
    #                 print(f"p={p}")
    #                 if D[p, p+1, q, n] >= p:
    #                     score += score + 1
    #             print(f"score[{p}, {q}] = {score}\n")
  

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


            
