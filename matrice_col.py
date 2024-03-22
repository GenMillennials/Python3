M = [[1, 2, 7, 3],
    [2, 4, 5, 3],
    [4, 5, 6, 6],
    [7, 8, 8, 9]]
n = len(M)
for i in range(n):
    for j in range(n):
        if (M[i][j] == max(M[i]) == min([M[k][j] for k in range(n)])
        or M[i][j] == min(M[i]) == max([M[k][j] for k in range(n)])):
            print("(", i, j,") = ", M[i][j])