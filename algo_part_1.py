s = "ABCBBCABABAC"
n = len(s)
A = [0] * n

for k in range(0, n):
    for a in range(k-1, -1, -1):
        if s[a] == s[k]:
            print("k: " + str(k), "& a: " + str(a))
            t = A[a]
            c = a + 1
            while (t < k) and (c < k):
                x = min(A[c], t)
                y = max(A[c], t)
                A[c] = x
                t = y
                c += 1
            A[a] = k
            print(A)

for i in range(len(A)):
    if A[i] != 0:
        A[i] += 1

print(A)

c = 0
l = 1
for k in range(0, n-2):
    t = 0
    for a in range(0, k-1):
        if A[a] > k:
            t = t + 1
    if t > c:
        c = t
        l = k
print(l)
    