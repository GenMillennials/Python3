n = int(input())
L = list(range(n + 1))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if 2 * i * j  + i + j < n:
            L[2 * i * j  + i + j] = 0
L = list(filter(lambda x: x > 0, L))
L = list(map(lambda x: 2 * x + 1, L))
L.insert(0, 2)
print(L)