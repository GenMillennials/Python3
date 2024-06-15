# Matrices multiplication
n, m =[int(i) for i in input().split()]
M1 = [[int(i) for i in input().split()] for j in range(n)]
input()
n2, m2 = [int(i) for i in input().split()]
M2 = [[int(i) for i in input().split()] for j in range(n2)]
M3 = [[0] * m2 for _ in range(n)]

for i in range(n):
    for q in range(m2):
        for k in range(m):
            M3[i][q] += M1[i][k] * M2[k][q]
        
for c in M3:
    print(*c)
