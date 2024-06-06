import os
import numpy as np

'''
# Populates the tensor T such that T[m][i][j][k][l] = f_m(i, j, k, l) 
# for all valid inputs and returns the populated tensor.
'''
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

'''
# Returns a list of tuples (p, q) such that T[n][p][p+1][q][q+1] 
# is maximized.
'''
def find_pq(T, n):
  # keys are ints (values of T), values are lists of tuples
  d = dict()
  for i in range(1, n):
    for k in range(i+1, n):
      if T[n][i][i+1][k][k+1] in d.keys():
        d[T[n][i][i+1][k][k+1]].append((i, k))
      else:
        d[T[n][i][i+1][k][k+1]] = [(i, k)]

  max_f = max(d.keys())
  # return dict value (list of tuples) corresponding to max key (T-value)
  return d[max_f]

'''
# Generates the f matrix for fixed values of m, j, l.
# Note: the leftmost column and top row correspond to i=0 and k=0, respectively, 
# so the leftmost column and top row will always consist entirely of 0s.
'''
def gen_F(T, j, l, m):
  F = np.zeros((j, l), dtype=int) 
  for i in range(1, j):
    for k in range (j, l):
      F[i, k] = T[m][i][j][k][l]
  return F

'''
# Generates the d matrix for fixed values of m, j, l.
# Note: the leftmost column and top row correspond to i=0 and k=0, respectively, 
# so the leftmost column and top row will always consist entirely of 0s.
'''
def gen_D(T, j, l, m):
  F = gen_F(T, j, l, m)
  D = np.zeros((j, l), dtype=int)
  for i in range(1, j):
    for k in range (j, l):
      D[i, k] = F[i, k] - F[i-1, k]
  return D

'''
# Generates the e matrix for fixed values of m, j, l.
# Note: the leftmost column and top row correspond to i=0 and k=0, respectively, 
# so the leftmost column and top row will always consist entirely of 0s.
'''
def gen_E(T, j, l, m):
  F = gen_F(T, j, l, m)
  E = np.zeros((j, l), dtype=int)
  for i in range(1, j):
    for k in range (j, l):
      E[i, k] = F[i, k] - F[i, k-1]
  return E 

'''
# Writes given parameters and f, d, e matrices to a text file which is stored in 
# a folder named after the given string and which has a file name consisting of 
# the j, l, m parameters. 
'''
def LCS(s, ideal, j, l, m):
  n = len(s)
  empty_T = np.zeros((n+1, n+1, n+1, n+1, n+1), dtype=int)
  # populate values of tensor T
  T = populate_T(empty_T, s)
  # extracts the largest tuple (p, q) s.t. T[n][p][p+1][q][q+1] is maximized
  p, q = find_pq(T, n)[-1]

  # select ideal j, l, m parameters
  if ideal:
    j, l, m = p+1, q+1, n
  # otherwise takes user-inputted parameters
  
  # generate f, d, and e two-dimensional matrices for fixed j, l, m
  params = (T, j, l, m)
  F = gen_F(*params) 
  D = gen_D(*params)
  E = gen_E(*params)

  # write to a file named after j, l, m params and stored in a folder named after the string
  file_name = str(f"results/{s}/ideal.txt") if ideal else str(f"results/{s}/{j}_{l}_{m}.txt")
  # folder is named after the string
  os.makedirs(os.path.dirname(file_name), exist_ok=True)
  file = open(file_name, "w")
  # display string and i, j, k, l, m parameters
  file.write(f"s = {s}\n\n")
  file.write(f"i is in range [1, {j})\n")
  file.write(f"j = {j}\n")
  file.write(f"k is in range [{j}, {l})\n")
  file.write(f"l = {l}\n")
  file.write(f"m = {m}\n")
  # display the substrings that would result from the split from the j, l, m values
  file.write(f"substrings: {s[0:j-1]}, {s[j-1:l-1]}, {s[l-1:m]}\n\n")
  # indicate the values of p and q if ideal parameters are requested
  if ideal:
    file.write(f"Values of p and q that maximize T[n][p][p+1][q][q+1]:\n\tp = {j-1}, q = {l-1}\n\n")
  # format and print the f, d, and e matrices (for specified j, l, m values)
  eq_signs = l * "="
  file.write(f"{eq_signs} F {eq_signs}\n")
  file.write(str(F) + '\n\n')
  file.write(f"{eq_signs} D {eq_signs}\n")
  file.write(str(D) + '\n\n')
  file.write(f"{eq_signs} E {eq_signs}\n")
  file.write(str(E))
  file.close()
  
  # inform the user of the name of their file
  print(f"\nYour file was saved: {file_name}\n")

'''
# Prompts user for an integer in the range (lower, upper) with exclusive bounds
# until a valid integer is entered and returns this valid integer. 
'''
def check_input(str_x, lower, upper):
  validInput = False
  while not validInput:
    try:
      x = int(input(f"{str_x}: "))
      if x > lower and x < upper:
        validInput = True
      else:
        print(f"Enter an integer in the proper range: {lower} < {str_x} < {upper}.")
    except ValueError:
      print("Enter a positive integer.")
  return x

##########################################################################################
# Interactive portion of the program
##########################################################################################
s = input("\nEnter string: ")
ideal = True if input("\nUse ideal parameters? (Yes/No): ").lower() == 'yes' else False

# case where user wants to select j, l, m parameters
if not ideal:
  print(f"\nEnter positive integers j, l, m. Note: 1 <= i < j <= k < l <= m <= {len(s)}.")
  # ensure that valid inputs are entered for j, l, m
  j = check_input("j", 1, len(s))
  l = check_input("l", j, len(s) + 1)
  m = check_input("m", l-1, len(s) + 1)
# otherwise user wants to use ideal parameters
else:
  j, l, m = 0, 0, 0

# write parameters and matrices to a text file
LCS(s, ideal, j, l, m)
