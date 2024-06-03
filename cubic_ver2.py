"""
LLCS - algorithm for the Length of the Longest Cubic Subsequence

"""

# a is length of seq1, b is length of seq2, c is length of seq3

count = 0
def LLCS(seq1, a, seq2, b, seq3, c, T):
    # track num of func calls
    global count
    count += 1
    # have not entered LLCS for a, b, c
    if T[a][b][c] == -1:
        if a == 0 or b == 0 or c == 0:
            T[a][b][c] = 0
        elif seq1[a-1] == seq2[b-1] == seq3[c-1]:
            T[a][b][c] = LLCS(seq1, a-1, seq2, b-1, seq3, c-1, T) + 1
        else:
            T[a][b][c] = max(   LLCS(seq1, a-1, seq2, b, seq3, c, T), 
                                LLCS(seq1, a, seq2, b-1, seq3, c, T), 
                                LLCS(seq1, a, seq2, b, seq3, c-1, T)    )
    # else we have stored a value for LLCS a, b, c
    print(T)
    return T[a][b][c]

def func(seq1, seq2, seq3):
    a, b, c = len(seq1), len(seq2), len(seq3)
    T = [ [ [-1 for x in range(c+1)] for y in range(b+1) ] for x in range(a+1) ]
    print(T)
    return LLCS(seq1, a, seq2, b, seq3, c, T)

"""seq1 = "abcb"
seq2 = "baaaacb"
seq3 = "bdacdb"         # longest cubic subsequence is bcb
"""

seq1 = "a"
seq2 = "aa"
seq3 = "a" 

whole_seq = "aaaa"

def main(whole_seq):
    # test all possible breakpoints
    k_list = []
    for x in range(len(whole_seq)):
        seq1 = whole_seq[:x]
        for z in range(x+1, len(whole_seq)):
            seq2 = whole_seq[x:z]
            seq3 = whole_seq[z:]
            k_list.append(func(seq1, seq2, seq3))
            print(f"seq1: {seq1}, seq2: {seq2}, seq3: {seq3}")
    print(k_list)
    return max(k_list)

ans = main(whole_seq)

print(f"{ans} is length of the LCS")
print(f"{count} is func call count")

