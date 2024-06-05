# This algorithm produces the LCS length, considering non-consecutive substrings 


# implement a function that returns the max element in table along with it's index in the table 


# Given a string s of length n, LCS(s) returns the length of the LCS 
def LCS(s):
  n = len(s)
  T = [[[[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]
  f(T, s)
  return m(T)
# allows us to index from i to n
# def changeStr(s):
#   return " " + s

# Given a table T, m(T) returns the maximum entry of T
def m(T):
  n = len(T)
  max = 0
  for m in range(0, n):
    for i in range(0, n):
      for j in range (0, n):
          for k in range (0, n):
            for l in range (0, n):
              if T[m][i][j][k][l] > 0:
                print(f"T[{m}][{i}][{j}][{k}][{l}] = {T[m][i][j][k][l]}")
              if T[m][i][j][k][l]> max:
                max =  T[m][i][j][k][l]
  return max
  

# Populates the table T with the values for each m, i, j, k, l combination 
def f(T, s):
  n = len(s)
  # s = changeStr(s)
  for m in range(1, n+1):
    # print("m", m)
    for i in range (1, m+1): 
      # print("i", i)
      for j in range(i+1, m+1):
        # print("j", j)
        for k in range(j, m+1): 
          # print("k", k)
          for l in range(k+1, m+1):
            # print("l", l)
            # case 1, character is matched
            # print()
            # print(f"m: {m}, i: {i}, j: {j}, k: {k}, l: {l}")
            # print("s[i-1] =", s[i-1],"s[j-1] =", s[j-1], "s[m-1] =", s[m-1])
            if s[i-1] == s[j-1] == s[m-1]: 
              # print("entered case 1")
              T[m-1][i-1][j-1][k-1][l-1] = T[m-1][i-2][j-1][k-1][l-1] + 1 
              # print("table val:", T[m-1][i-1][j-1][k-1][l-1])
            # case 2, character is not matched 
            else:
              # print("entered case 2")
              T[m-1][i-1][j-1][k-1][l-1]= max(T[m-1][i-2][j-1][k-1][l-1], 
                                              T[m-1][i-1][j-2][k-1][l-1], 
                                              T[m-2][i-1][j-1][k-1][l-1])
                      

print(LCS('aaaaaa'))
#Correct for aaa, ababab