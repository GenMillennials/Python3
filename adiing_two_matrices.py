# Adding two matrices
x = input().split()
n, m = int(x[0]), int(x[1])
M = [[int(x) for x in input().split()] for _ in range(n)]
z = input()                                                 # to paste an empty string
M1 = [[int(x) for x in input().split()] for _ in range(n)]
M2 = [[int(x) for x in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        M2[i][j] = M[i][j] + M1[i][j]

for i in range(n):
    print(*M2[i])
