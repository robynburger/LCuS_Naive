# Two Case

whole_seq = "abcadbab"  # longest seq is 2 - ab

def helper(seq):
    n = len(seq)
    # T is 0...n-1 for each set of indices
    T = [[[0 for x in range(n+1)] for y in range(n+1)] for z in range(n+1)]
    # populates T
    T = f(seq, T)
    print(T)

# populates T table
def f(seq, T):
    n = len(seq)
    # seq is 0...n-1  --> with n indices
    for k in range(n):     # 0...n-1
        for i in range(n):     # 0...n-1
            for j in range(i+1, n):      # i+1...n-1
                if seq[i] == seq[k]:        # 0...n-1
                    T[i][j][k] = T[i-1][j][k-1] + 1
                else:
                    T[i][j][k] = max(T[i-1][j][k], T[i][j][k-1])
    return T

helper(whole_seq)
                    