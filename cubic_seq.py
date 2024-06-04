# # Reccurence Relation:
# # def LTCS(i, j, k, l, m):
# #   #case 1 
# #   if 1 <= i and i < j and j <= k and k < l and l <= m:
# #     return LCM(i, j, k, l, m)

# #   #case 2
# #   if i >= 0 and j >= 0 and k >= 0 and l >= 0:
# #     return 0;

# #   #case 3
# #   if i < 0 or j < 0 or k < 0 or l < 0:
# #     return -1
  
# # def LCM(i, j, k, l):
# #   return 0


# #Dynamic Programming

# # Given string of characters s= (s[0], s[2], ..., s[m]), LTCS(s) returns the 
# # length of the longest tandem cubic tandem subsequence
# mem = []

# def LTCS(s):
#   le = len(s)  # 1-based length of input string s
#   m = le - 1
#   global mem
#   mem = [[[[[-1 for _ in range(m+1)] for _ in range(m+1)] for _ in range(m+1)] for _ in range(m+1)] for _ in range(m+1)]
#     # Filling in memoization table
#   for l in range (0, le):
#     for k in range (0, l):
#         for j in range (0, k+1): # need?
#            for i in range (0, j):
#             f(s, i, j, k, l, m)
#   return mem

# def f(s, i, j, k, l, m):
#   global mem
# # case 1 
#   print("i=", i, "j=", j, "k=", k, "l=", l)
#   if 0 <= i < j <= k < l <= m: 
#     if s[i] == s[k] == s[j]:
#       print("case 1")
#       mem[i][j][k][l][m] = mem[i-1][j][k-1][l][m] + 1
#       print("mem[i][j][k][l][m]= ", mem[i][j][k][l][m])

#     elif i >= 0 and j >= 0 and k >= 0 and l >= 0:
#       print("case 1.1")
#       # print("mem[i-1][j][k][l][m] = ", mem[i-1][j][k][l][m])
#       if mem[i-1][j][k][l][m] == -1 or mem[i-1][j][k][l][m] == -2:

#         mem[i-1][j][k][l][m] =f (s, i-1, j, k, l, m)
#       if mem[i][j][k-1][l][m] == -1 or mem[i][j][k-1][l][m] == -2:
#         mem[i][j][k-1][l][m] = f(s, i, j, k-1, l, m)
#       if mem[i][j][k][l][m-1] == -1 or mem[i][j][k][l][m-1] == -2:
#         mem[i][j][k][l][m-1] = f(s, i, j, k, l, m-1)
#       mem[i][j][k][l][m] = max(mem[i-1][j][k][l][m], mem[i][j][k-1][l][m],mem[i][j][k][l][m-1])
#       print("mem[i][j][k][l][m]= ", mem[i][j][k][l][m])

# # case 2
#   if i >= -1 and j >= -1 or k >= -1 or l >= -1 or m >= -1:
#     print("case 2")
#     mem[i][j][k][l][m] = 0
#     print("mem[i][j][k][l][m]= ", mem[i][j][k][l][m])
# # case 3 
#   if i < -1 or j < -1 or k < -1 or l < -1 or m < -1:
#     print("case 3")
#     mem[i][j][k][l][m] = -2
#     print("mem[i][j][k][l][m]= ", mem[i][j][k][l][m])

# print("Test: ", LTCS('abcabcabc'))