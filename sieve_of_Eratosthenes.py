n = int(input())
L = list(range(n + 1))
for i in range(2, n + 1):
    if L[i] != 0:
        for j in range(L[i] * 2, n + 1, L[i]):   # Dividers of 2
            L[j] = 0
L = sorted(list(set(L)))   # Delete all nulles in the list
print(L)