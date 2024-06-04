# Two Case

whole_seq = "abcadbab"  # longest seq is 2 - ab

def helper(seq):
    n = len(seq)
    # T is 0...n-1 for each set of indices
    T = [[[0 for x in range(n)] for y in range(n)] for z in range(n)]
    # populates T
    f(seq, T)
    print(T)

# populates T table
def f(seq, T):
    n = len(seq)
    # seq is 0...n-1  --> with n indices
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                if seq[i-1] == seq[k-1]:
                    T[k][i][j] = T[k-1][i-1][j]