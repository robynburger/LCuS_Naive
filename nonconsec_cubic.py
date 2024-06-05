# Given a string s of length n, LCS(s) returns the length of the LCS 
import numpy as np

def LCS(s):
  n = len(s)
  T = np.zeros((n+1, n+1, n+1, n+1, n+1))
  f(T, s)
  return np.max(T)

# LOOP OVER P, Q in T and find those that are the max
def f(T, s):
  n = len(s)
  for m in range(1, n+1):
    for i in range (1, m+1): 
      for j in range(i+1, m+1):
        for k in range(j, m+1): 
          for l in range(k+1, m+1):
            if s[i-1] == s[k-1] == s[m-1]: 
              T[m][i][j][k][l] = T[m-1][i-1][j][k-1][l] + 1 
            else:
                T[m][i][j][k][l]= max(T[m][i-1][j][k][l], 
                                              T[m][i][j][k-1][l], 
                                              T[m-1][i][j][k][l])
print(LCS("aabcabbcfabc"))
