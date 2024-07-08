import random
import numpy as np

# gamma(m, x, seq) is the largest value of r such that r <= x and 
# seq[r] == seq[m], or 0 if no such value exists

# characters allowed in test string 
alphabet = ['a', 'b', 'c']

# max size of the test string 
max_length = 10

# number of test cases
num_tests = 1000000000

def gamma(m, x, seq):
    for r in range(x, 0, -1):
        if seq[r-1] == seq[m-1]:
            return r
    return 0

def check_j(j_vec, i): 
    first_one_index = -1
    last_one_index = -1
    for x in range(len(j_vec)):
      if j_vec[x] == 1:
        if first_one_index == -1:
            first_one_index = x
            last_one_index = x
        else: 
            last_one_index = x
    for y in range(first_one_index, last_one_index +1):
        if j_vec[y] != 1:
            return False
    if first_one_index == i+1 or first_one_index == -1:
        return True
    else: 
        print(f"First one at {first_one_index}, but i+1 = {i+1}")
        return False 

def gen_j_vector(seq, count):
    n = len(seq)
    f = np.zeros((n+1, n+1, n+1, n+1, n+1), dtype=int)      # f[m,j,i,k,l]

    # for each j, i, k
    for m in range(1, n+1):
        for l in range(3, n+1):
            for k in range(2, l):
                for i in range(1, k):
                    j_vector = np.zeros((n+1), dtype=int)
                    # Populate j vector for given i,k,l
                    for j in range(i+1, k):
                        f[n, j, i, k, l] = f[n - 1, j, i, k, l]
                        if gamma(n, i, seq) > 0 and gamma(n, k, seq) >= j:
                            f[n, j, i, k, l] = max(f[n, j, i, k, l], f[n-1, j, gamma(n, i, seq)-1, gamma(n, k, seq)-1, l]+1)
                
                        j_vector[j] = f[n, j, i, k, l] - f[n, j, i-1, k, l]
                    # Check 1s are contiguous 
                    if np.any(j_vector) == 1 and not check_j(j_vector, i):
                        print(f"Test {count}: Fail {seq}")
                        print(f"m: {m}, j: {j}, i: {i}, k: {k}")
                        print(j_vector)
                        print("\n")
                        return False
    # count = count + 1
    if count % 1000 == 0:
        print(f"Pass {count}")
    return True
        
not_failed = True
for x in range(num_tests):
  if not_failed:
    seq = ""
    for _ in range(random.randint(max_length-5, max_length)):
      seq += str(random.choice(alphabet))
    not_failed = gen_j_vector(seq, x)