# Three Case
import numpy as np

whole_seq = "abbbcfafafbfcabc"  # longest seq is 2 - ab

def helper(seq):
    n = len(seq)
    # T is 0...n-1 for each set of indices
    T = np.array([[[[[0 for a in range(n)] for b in range(n)] for c in range(n)] for d in range(n)] for e in range(n)])
    # populates T
    T = f(seq, T)
    #print(T)
    print(T.max())

# populates T table
def f(seq, T):
    n = len(seq)
    # seq is 0...n-1  --> with n indices
    for m in range(n):     # 0...n-1
        for i in range(m+1):     # 0...m
            for j in range(i+1, m+1):      # i+1...m
                for k in range(j, m+1):         # j...m
                    for l in range(k+1, m+1):       # k+1...m
                        a, b, c = i-1, k-1, m-1
                        if seq[i] == seq[k] == seq[m]:        # 0...n-1      
                            if a == -1 or b == -1 or c == -1:
                                T[m, i, j, k, l] = 1      # because T[m-1, i-1, j, k-1, l] = 0
                            else: 
                                T[m, i, j, k, l] = T[m-1, i-1, j, k-1, l] + 1     # possible that i-1, k-1 < 0
                        else:
                            if a < 0 and b < 0 and c < 0:
                                T[m, i, j, k, l] = 0
                            elif a < 0:
                                if b < 0:
                                    T[m, i, j, k, l] = T[m-1, i, j, k, l]
                                elif c < 0:
                                    T[m, i, j, k, l] = T[m, i, j, k-1, l]
                                else:
                                    T[m, i, j, k, l] = max( T[m, i, j, k-1, l], 
                                                            T[m-1, i, j, k, l])
                            elif b < 0:
                                if c < 0:
                                    T[m, i, j, k, l] = T[m, i-1, j, k, l]
                                else:
                                    T[m, i, j, k, l] = max( T[m, i-1, j, k, l], 
                                                            T[m-1, i, j, k, l])
                            elif c < 0:
                                T[m, i, j, k, l] = max( T[m, i-1, j, k, l], 
                                                        T[m, i, j, k-1, l])
                            else:
                                T[m, i, j, k, l] = max(T[m, i-1, j, k, l], 
                                                       T[m, i, j, k-1, l], 
                                                       T[m-1, i, j, k, l])
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