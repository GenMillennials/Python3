# Matrice exponentiation
n = int(input())
M1 = [[int(i) for i in input().split()] for j in range(n)]
M2 = M1
x = int(input())
for _ in range(x - 1):
    M3 = [[0] * n for j in range(n)]
    for i in range(n):
        for q in range(n):
            for k in range(n):
                M3[i][q] += M1[i][k] * M2[k][q]
    M1 = M3

for c in M3:
    print(*c)
