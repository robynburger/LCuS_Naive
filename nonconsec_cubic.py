# This algorithm produces the LCS length, considering non-consecutive substrings 
global T

# Given a string s of length n, LCS(s) returns the length of the LCS 
def LCS(s):
  n = len(s) 
  global T 
  T = [[[[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]
  f(T, s, n, n, n, n, n)
  return T#[n-1][n-1][n-1][n-1][n-1]

# Updates the table T with the values for each m, i, j, k, l combination 
def f(T, s,  m, i, j, k, l):
  n = len(s)
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
            if s[i-1] == s[j-1] == s[m-1]: 
              print("entered case 1, m, i, j, k,l", m, i, j, k, l)
              T[m][i][j][k][l] = T[m][i-1][j][k][l] + 1 
            # case 2, character is not matched 
            else:
              print("entered case 2, m, i, j, k,l", m, i, j, k, l)
              T[m-1][i-1][j-1][k-1][l-1]= max(T[m][i-2][j-1][k-1][l-1], T[m-1][i-1][j-2][k-1][l-1], T[m-1][i-1][j-1][k-2][l-1])
                      

print(LCS('aaa'))