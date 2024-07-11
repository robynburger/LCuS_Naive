import random
import numpy as np

# characters allowed in test string 
alphabet = ['a', 'b', 'c', 'd']

# max size of the test string 
max_length = 10

# number of test cases
num_tests = 1

def gamma(m, x, seq):
    for r in range(x, 0, -1):
        if seq[r-1] == seq[m-1]:
            return r
    return 0

def check_l(l_vec, k): 
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
    if first_one_index == k+1 or first_one_index == -1:
        return True
    else: 
        print(f"First 1 at index {first_one_index}, but k+1 = {k+1}")
        return False 

def gen_l(seq, count):
    n = len(seq)
    f = np.zeros((n+1, n+1, n+1, n+1, n+1), dtype=int)      # f[m,j,i,k,l]

    # for each j, m, i, k
    for m in range(1, n+1):
        for i in range(1, n):
            for k in range(i+1, n):
                for j in range(i+1, k+1):

                    l_vector = np.zeros((n+1), dtype=int)
                    for l in range(k+1, m+1):
                        f[m, j, i, k, l] = f[m - 1, j, i, k, l]
                        if gamma(m, i, seq) > 0 and gamma(m, k, seq) >= j:
                            f[m, j, i, k, l] = max(f[m, j, i, k, l], f[m-1, j, gamma(m, i, seq)-1, gamma(m, k, seq)-1, l]+1)

                        l_vector[l] = f[m, j, i, k, l] - f[m, j, i, k-1, l]

                    # check 1s are contiguous
                    if np.any(l_vector) == 1 and not check_l(l_vector, k):
                        print(f"Test {count}: Fail {seq}")
                        print(f"m: {m}, j: {j}, i: {i}, k: {k}")
                        print(l_vector)
                        print("\n")

    count = count + 1
    if count % 1000 == 0:
        print(f"Pass {count}")
    return True
        
not_failed = True
for x in range(num_tests):
    if not_failed:
        seq = ""
        for _ in range(random.randint(max_length-5, max_length)):
            seq += str(random.choice(alphabet))
        seq = "cdababcdacbd"
    not_failed = gen_l(seq, x)