import numpy as np

# gamma(m, x, seq) is the largest value of r such that r <= x and 
# seq[r] == seq[m], or 0 if no such value exists
def gamma(m, x, seq):
    for r in range(x, 0, -1):
        if seq[r-1] == seq[m-1]:
            return r
    return 0

def test_l(seq):
    n = len(seq)
    f = np.zeros((n+1, n+1, n+1, n+1, n+1), dtype=int)      # f[m,j,i,k,l]

    # for each j, m, i, k
    for m in range(1, n+1):
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                for k in range(j, n+1):
                    l_vector = np.zeros((n+1), dtype=int)
                    for l in range(k+1, m+1):
                        f[m, j, i, k, l] = f[m - 1, j, i, k, l]
                        if gamma(m, i, seq) > 0 and gamma(m, k, seq) >= j:
                            f[m, j, i, k, l] = max(f[m, j, i, k, l], f[m-1, j, gamma(m, i, seq)-1, gamma(m, k, seq)-1, l]+1)
                        l_vector[l-1] = f[m, j, i, k, l] - f[m, j, i-1, k-1, l]
                        
                    if np.any(l_vector) == 1:
                        print(f"m: {m}, j: {j}, i: {i}, k: {k}")
                        print(l_vector)
                        print("\n")


                        """ non_zero = False
                        for x in range(n+1):
                            if l_vector[x, 1] == 1:
                                non_zero = True
                        if non_zero:
                            print(l_vector)"""

test_l("abcadbabyc")