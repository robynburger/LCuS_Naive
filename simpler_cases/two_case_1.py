"""
LLTS - algorithm for the Length of the Longest Tandem Subsequence

"""
count = 0

def LLTS(seq1, m, seq2, n, T):
    # track num of recursive calls
    global count 
    count += 1
    # have not entered LLTS for m, n
    if T[m][n] == -1:
        if m == 0 or n == 0:
            T[m][n] = 0
        elif seq1[m-1] == seq2[n-1]:
            T[m][n] = LLTS(seq1, m-1, seq2, n-1, T) + 1
        else:
            T[m][n] = max(LLTS(seq1, m-1, seq2, n, T), LLTS(seq1, m, seq2, n-1, T))
    # else we have stored a value for LLTS m, n
    print(T)
    return T[m][n]

def func(seq1, seq2):
    m, n = len(seq1), len(seq2)
    T = [ [-1 for i in range(n+1)] for j in range(m+1) ]
    return LLTS(seq1, m, seq2, n, T)

# seq1 = "holiday"
# seq2 = "echoed"

whole_seq = "holidayechoed"

def main(whole_seq):
    # test m + n breakpoints
    k_list = []
    for z in range(len(whole_seq)):
        seq1 = whole_seq[:z]
        seq2 = whole_seq[z:]
        k_list.append(func(seq1, seq2))
    print(k_list)
    return max(k_list)

ans = main(whole_seq)

print(f"{ans} is length of the LTS")
print(f"{count} is func call count")

