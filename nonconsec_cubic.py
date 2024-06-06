import numpy as np

def find_pq(T, n):
  m = n
  d = dict()

  for i in range(1, m):
    for k in range(i+1, m):
      if T[m][i][i+1][k][k+1] in d.keys():
        d[T[m][i][i+1][k][k+1]].append((i, k))
      else:
        d[T[m][i][i+1][k][k+1]] = [(i, k)]
  
  max_f = max(d.keys())
  return d[max_f]

# populate_T(T, s) modifies T[m][i][j][k][l] to be f_m(i, j, k, l) for all valid inputs
def populate_T(T, s):
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
  return T
# generates the f matrix for fixed values of m, j, l
# Note: leftmost column and top row correspond to i= 0 and k=0, respectively 
# so the leftmost column and top row will always be 0s
def gen_F(T, j, l, m):
  F = np.zeros((j, l), dtype=int) 
  for i in range(1, j):
    for k in range (j, l):
      F[i, k] = T[m][i][j][k][l]
  return F

# gen_D generates the D matrix for the fixed jalues of m, j, l
# Note: leftmost column and top row correspond to i= 0 and k=0, respectively 
# so the leftmost column and top row will always be 0s
def gen_D(T, j, l, m):
  F = gen_F(T, j, l, m)
  D = np.zeros((j, l), dtype=int)
  for i in range(1, j):
    for k in range (j, l):
      D[i, k] = F[i, k] - F[i-1, k]
  return D

# gen_E generates the E matrix for the fixed jalues of m, j, l
# Note: leftmost column and top row correspond to i= 0 and k=0, respectively 
# so the leftmost column and top row will always be 0s
def gen_E(T, j, l, m):
  F = gen_F(T, j, l, m)
  E = np.zeros((j, l), dtype=int)
  for i in range(1, j):
    for k in range (j, l):
      E[i, k] = F[i, k] - F[i, k-1]
  return E 

# Given a string s of length n, LCS(s) returns the length of the LCS 
def LCS(s):
  n = len(s)
  t = np.zeros((n+1, n+1, n+1, n+1, n+1), dtype=int)
  T = populate_T(t, s)
  p, q = find_pq(T, n)[-1]
  params = (T,p+1, q+1, n)
  F = gen_F(*params) 
  D = gen_D(*params)
  E = gen_E(*params)

  file = open(f"{s}.txt", "w")
  file.write(f"s = {s}\n \n")
  file.write(f"p = {p}\n \n")
  file.write(f"q = {q}\n \n")
  file.write('==== F =====\n')
  file.write(str(F) + '\n \n')
  file.write('==== D ===== \n')
  file.write(str(D) + '\n \n')
  file.write('==== E =====\n')
  file.write(str(E))
  file.close()
  # f.write(f"j = {5}")
  # f.write(f"l = {10}")
  # print(gen_D(T, 4, 6, n))
  # for m in range(1, n+1):
  #   #F.tofile('prelim_results.txt', sep='', format='%s')  
  #   return find_pq(T, len(s))
  # print('F')
  # print(F)
  # print('D')
  # print(D)
  # print('E')
  # print(E)

# find_pq(T, n) returns a list of tuples (p,q) such that T[m][p][p+1][q][q+1] is
# maximized

  
LCS("abcabab")
# print(ans)
