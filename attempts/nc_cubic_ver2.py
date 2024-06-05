# Three Case - algorithm which computes the length of the LCS (Longest Cubic Subsequence) 

import numpy as np

whole_seq = "aabbavaaa"

# initializes T array (5-d multidimensional array)
def helper(seq):
    n = len(seq)
    # T is 0...n-1 for each set of indices
    T = np.zeros((n, n, n, n, n))
    # f populates values of T
    T = f(seq, T)
    return T

# populates T table
def f(seq, T):
    n = len(seq)
    # seq is 0...n-1 with length n
    for m in range(n):     # 0...n-1
        for i in range(m+1):     # 0...m
            for j in range(i+1, m+1):    # i+1...m
                for k in range(j, m+1):         # j...m
                    for l in range(k+1, m+1):       # k+1...m
                        # verify that potential indices are not -1
                        a, b, c = i-1, k-1, m-1
                        # characters are the same
                        if seq[i] == seq[k] == seq[m]:      
                            if a == -1 or b == -1 or c == -1:
                                T[m, i, j, k, l] = 1    # because T[m-1, i-1, j, k-1, l] = 0
                            else: 
                                T[m, i, j, k, l] = T[m-1, i-1, j, k-1, l] + 1   # possible that m-1, i-1, k-1 < 0
                        # characters are not the same
                        else:
                            # max(0, 0, 0) is 0
                            if a < 0 and b < 0 and c < 0:
                                T[m, i, j, k, l] = 0
                            elif a < 0:
                                # max(0, 0, x) is x
                                if b < 0:
                                    T[m, i, j, k, l] = T[m-1, i, j, k, l]
                                elif c < 0:
                                    T[m, i, j, k, l] = T[m, i, j, k-1, l]
                                # max(0, x, y) is max(x, y)
                                else:
                                    T[m, i, j, k, l] = max( T[m, i, j, k-1, l], 
                                                            T[m-1, i, j, k, l])
                            elif b < 0:
                                # max(0, 0, x) is x
                                if c < 0:
                                    T[m, i, j, k, l] = T[m, i-1, j, k, l]
                                # max(0, x, y) is max(x, y)
                                else:
                                    T[m, i, j, k, l] = max( T[m, i-1, j, k, l], 
                                                            T[m-1, i, j, k, l])
                            elif c < 0:
                                # max(0, x, y) is max(x, y)
                                T[m, i, j, k, l] = max( T[m, i-1, j, k, l], 
                                                        T[m, i, j, k-1, l])
                            else:
                                T[m, i, j, k, l] = max(T[m, i-1, j, k, l], 
                                                       T[m, i, j, k-1, l], 
                                                       T[m-1, i, j, k, l])
    return T

# print(helper(whole_seq).max())

# returns list of all the possible (i, j, k, l) tuples which match the target
def index_tuples(seq):
    # LOOP OVER P, Q in T and find those that are the max
    T = helper(seq)
    target = T.max()
    n = len(seq)
    list_indices = []
    m = n-1
    for i in range(m+1):     # 0...m
        for j in range(i+1, m+1):    # i+1...m
            for k in range(j, m+1):         # j...m
                for l in range(k+1, m+1):
                    if T[m, i, j, k, l] == target:
                        list_indices.append((i, j, k, l))
    return list_indices

# return possible i, k indices which would split the sequence most optimally
def answer(seq):
    list_possible = index_tuples(seq)
    list_ans = [(i, k) for i, j, k, l in list_possible if i==j-1 and k==l-1]
    return list_ans


l = answer(whole_seq)
print(l)

T = helper(whole_seq)
print(T)
