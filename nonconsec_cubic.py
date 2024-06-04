# This algorithm produces the LCS length, considering non-consecutive substrings 

# Given a string s of length n, LCS(s) returns the length of the LCS 
def LCS(s):
  n = len(s)
  T = [[[[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]
  f(T, s)
  # returns value in bottom right corner
  return T[n-1][n-1][n-1][n-1][n-1]

# allows us to index from i to n
def changeStr(s):
  return " " + s

# Populates the table T with the values for each m, i, j, k, l combination 
def f(T, s):
  n = len(s)
  s = changeStr(s)
  for m in range(1, n+1):
    print("m", m)
    for i in range (1, m+1): 
      print("i", i)
      for j in range(i+1, m+1):
        print("j", j)
        for k in range(j, m+1): 
          print("k", k)
          for l in range(k+1, m+1):
            print("l", l)
            # case 1, character is matched
            print("hello2")
            if s[i] == s[j] == s[m]: 
              print(f"entered case 1 - m: {m}, i: {i}, j: {j}, k: {k}, l: {l}")
              T[m-1][i-1][j-1][k-1][l-1] = T[m-1][i-2][j-1][k-1][l-1] + 1 
              print("table val:", T[m-1][i-1][j-1][k-1][l-1])
            # case 2, character is not matched 
            else:
              print(f"entered case 2 - m: {m}, i: {i}, j: {j}, k: {k}, l: {l}")
              T[m-1][i-1][j-1][k-1][l-1]= max(T[m-1][i-2][j-1][k-1][l-1], 
                                              T[m-1][i-1][j-2][k-1][l-1], 
                                              T[m-2][i-1][j-1][k-1][l-1])
                      

print(LCS('aaa'))