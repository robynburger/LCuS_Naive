# Reccurence Relation:
# def LTCS(i, j, k, l, m):
#   #case 1 
#   if 1 <= i and i < j and j <= k and k < l and l <= m:
#     return LCM(i, j, k, l, m)

#   #case 2
#   if i >= 0 and j >= 0 and k >= 0 and l >= 0:
#     return 0;

#   #case 3
#   if i < 0 or j < 0 or k < 0 or l < 0:
#     return -1
  
# def LCM(i, j, k, l):
#   return 0


#Dynamic Programming

# Given string of characters s= (s[0], s[2], ..., s[m]), LTCS(s) returns the 
# length of the longest tandem cubic tandem subsequence
mem = []

def LTCS(s):
  ans = 0  # greatest length subsequence so far
  le = len(s)  # 1-based length of input string s
  m = le - 1
  global mem
  mem = [[[[[-1 for _ in range(m+1)] for _ in range(m+1)] for _ in range(m+1)] for _ in range(m+1)] for _ in range(m+1)]
    # Filling in memoization table
  for i in range (0, le):
    for j in range(0, le):
      for k in range(0, le):
        for l in range(0, le):
           f(s, i, j, k, l, m)
  return mem[m][m][m][m][m]

def f(s, i, j, k, l, m):
  global mem
# case 1
  if 0 <= i < j <= k < l <= m: 
    if s[i] == s[k] == s[j]:
      return f(s, i-1, j, k-1, l, m) + 1
    else:
      if mem[i-1][j][k][l][m] == -1:
        mem[i-1][j][k][l][m] =f (s, i-1, j, k, l, m)
      if mem[i][j][k-1][l][m] == -1:
        mem[i][j][k-1][l][m] = f(s, i, j, k-1, l, m)
      if mem[i][j][k][l][m-1] == -1:
        mem[i][j][k][l][m-1] = f(s, i, j, k, l, m-1)
      return max(mem[i-1][j][k][l][m], mem[i][j][k-1][l][m],mem[i][j][k][l][m-1])
# case 2
  if i >= -1 and j >= -1 or k >= -1 or l >= -1 or m >= -1:
    return 0
# case 3 
  if i < -1 or j < -1 or k < -1 or l < -1 or m < -1:
    return -1 
  
print("Test: ", LTCS('aaa'))