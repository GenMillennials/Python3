n = int(input())   # n > k
k = int(input())   # k < n
L = [i for i in range(1, n + 1)]
while len(L) > 1:
    for j in range(0, k - 1):
        L.append(L[j])
    del L[:k]
print(*L)