import random
import numpy as np

# gamma(m, x, seq) is the largest value of r such that r <= x and 
# seq[r] == seq[m], or 0 if no such value exists

# characters allowed in test string 
alphabet = ['a', 'b', 'c', 'd']

# max size of the test string 
max_length = 10

# number of test cases
num_tests = 500

def gamma(m, x, seq):
    for r in range(x, 0, -1):
        if seq[r-1] == seq[m-1]:
            return r
    return 0


def check_l(l_vec): 
    first_one_index = -1
    last_one_index = -1
    for x in range(len(l_vec)):
      if l_vec[x] == 1:
        if first_one_index == -1:
            first_one_index = x
            last_one_index = x
        else: 
            last_one_index = x
    for y in range(first_one_index, last_one_index +1):
        if l_vec[y] != 1:
            return False
    return True

def gen_l(seq):
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
                            if seq[i-1] == seq[k-1]: 
                              l_vector[l] = f[m, j, i, k, l] - f[m, j, i-1, k-1, l]
                    # l_vector = np.array([0, 1, 0, 1, 0])
                    if np.any(l_vector) == 1 and not check_l(l_vector):
                        print(f"{seq}")
                        print(f"m: {m}, j: {j}, i: {i}, k: {k}")
                        print(l_vector)
                        print("\n")
                        return False
    print(f"Pass {seq}")
    return True
        
not_failed = True
for _ in range(num_tests):
  while not_failed:
    seq = ""
    for _ in range(random.randint(3, max_length)):
      seq += str(random.choice(alphabet))
    not_failed = gen_l(seq)