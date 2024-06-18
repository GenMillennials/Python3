# Filling in the matrice as a snake sequence

x = input().split()
n, m = int(x[0]), int(x[1])
M = []
for _ in range(n):
    val = [c for c in range(m)]
    M.append(val)

count = 1
for i in range(n):
    for j in range(m):
        M[i][j] = count
        count += 1

for i in range(n):
    if i % 2 != 0:
        M[i].reverse()
        
for i in range(n):
    for j in range(m):
        print(str(M[i][j]).ljust(3), end=" ")
    print()
