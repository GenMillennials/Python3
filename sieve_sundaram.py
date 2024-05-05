n = int(input())
L = list(range(n + 1))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if 2 * i * j  + i + j < n:
            L[2 * i * j  + i + j] = 0
L = [el for el in L if el > 0]
for i in range(len(L)):
    L[i] = 2 * L[i] + 1
print(L)