import os
import numpy as np

# find_pq(T, n) returns a list of tuples (p,q) such that T[m][p][p+1][q][q+1] is
# maximized
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
# gen_F(T, j, l, m) generates the f matrix for fixed values of m, j, l
# Note: leftmost column and top row correspond to i= 0 and k=0, respectively 
# so the leftmost column and top row will always be 0s
def gen_F(T, j, l, m):
  F = np.zeros((j, l), dtype=int) 
  for i in range(1, j):
    for k in range (j, l):
      F[i, k] = T[m][i][j][k][l]
  return F

# gen_D(T, j, l, m) generates the D matrix for the fixed jalues of m, j, l
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

# LCS a string s of length n, LCS(s) writes parameters and F, D, E matrices to a file
def LCS(s, ideal, j, l, m):
  n = len(s)
  t = np.zeros((n+1, n+1, n+1, n+1, n+1), dtype=int)
  T = populate_T(t, s)

  # extracts the largest tuple from the list of tuples
  p, q = find_pq(T, n)[-1]

  # select parameters
  if ideal:
    j, l, m = p+1, q+1, n
  # otherwise takes inputted params (function arguments)2

  params = (T, j, l, m)

  F = gen_F(*params) 
  D = gen_D(*params)
  E = gen_E(*params)

  # indicate ideal or not in name of the test file
  ind = "not_ideal"
  if ideal:
    ind = "ideal"

  # writes results to a file
  file_name = str(f"results/{s}/ideal.txt") if ideal else str(f"results/{s}/{j}_{l}_{m}.txt")
  os.makedirs(os.path.dirname(file_name), exist_ok=True)
  file = open(file_name, "w")
  file.write(f"s = {s}\n\n")
  file.write(f"i is in range [1, {j})\n")
  file.write(f"j = {j}\n")
  file.write(f"k is in range [{j}, {l})\n")
  file.write(f"l = {l}\n")
  file.write(f"m = {m}\n")
  file.write(f"substrings: {s[0:j-1]}, {s[j-1:l-1]}, {s[l-1:m]}\n\n")
  if ideal:
    file.write(f"Values of p and q that maximize T[n][p][p+1][q][q+1]:\n\tp = {j-1}, q = {l-1}\n\n")
  eq_signs = l * "="
  file.write(f"{eq_signs} F {eq_signs}\n")
  file.write(str(F) + '\n\n')
  file.write(f"{eq_signs} D {eq_signs}\n")
  file.write(str(D) + '\n\n')
  file.write(f"{eq_signs} E {eq_signs}\n")
  file.write(str(E))
  file.close()
  print(f"\nYour file was saved: {file_name}\n")

# prompts user for an integer in the range (lower, upper) with exclusive bounds
def check_input(str_x, lower, upper):
  validInput = False
  while not validInput:
    try:
      x = int(input(f"{str_x}: "))
      if x > lower and x < upper:
        validInput = True
      else:
        print("Enter an integer in the proper range.")
    except ValueError:
      print("Enter a positive integer.")
  return x

  
s = input("\nEnter string: ")

ideal = True if input("\nUse ideal parameters? (Yes/No): ").lower() == 'yes' else False

# Case 1: user selects parameters. s
if not ideal:
  print(f"\nEnter positive integers j, l, m. Note: 1 <= i < j <= k < l <= m <= {len(s)}.")
  
  j = check_input("j", 1, len(s))
  l = check_input("l", j, len(s) + 1)
  m = check_input("m", l-1, len(s) + 1)
  
# Case 2: uses ideal parameters. Initially set to 0, but updated in LCS. 
else:
  j, l, m = 0, 0, 0


LCS(s, ideal, j, l, m)

