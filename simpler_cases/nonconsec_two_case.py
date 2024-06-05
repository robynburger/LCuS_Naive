# Two Case
import numpy as np

whole_seq = "babbca"  # longest seq is 2 - ab

def helper(seq):
    n = len(seq)
    # T is 0...n-1 for each set of indices
    T = np.array([[[0 for x in range(n)] for y in range(n)] for z in range(n)])
    # populates T
    T = f(seq, T)
    print(T)

# populates T table
def f(seq, T):
    n = len(seq)
    # seq is 0...n-1  --> with n indices
    for k in range(n):     # 0...n-1
        for i in range(k+1):     # 0...k                   0 <= i <= k
            for j in range(i+1, k+1):      # i+1...k       i < j <= k
                a, b = i-1, k-1
                if seq[i] == seq[k]:        # 0...n-1      
                    if a == -1 or b == -1:
                        T[k, i, j] = 1      # because T[k=1, i-1, j] = 0
                    else: 
                        T[k, i, j] = T[k-1, i-1, j] + 1     # possible that i-1, k-1 < 0
                else:
                    if a < 0 and b < 0:
                        T[k, i, j] = 0
                    elif a < 0:
                        T[k, i, j] = T[k-1, i, j]
                    elif b < 0:
                        T[k, i, j] = T[k, i-1, j]
                    else:
                        T[k, i, j] = max(T[k, i-1, j], 
                                         T[k-1, i, j])
    return T

helper(whole_seq)

"""
n = 6
B = np.array([[[0 for x in range(n)] for y in range(n)] for z in range(n)])
for k in range(n):     # 0...n-1
        for i in range(n):     # 0...n-1
            for j in range(i+1, n): 
                B[0, 1, 2] = 3
                # B[k, i, j]
print(B)
"""