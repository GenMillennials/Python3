M = [[1, 2, 7, 3],
    [2, 4, 5, 3],
    [4, 5, 6, 6],
    [7, 8, 8, 9]]
n = len(M)
maxrow = [max(M[i]) for i in range(n)]
minrow = [min(M[i]) for i in range(n)]
maxcol = [max([M[j][i] for j in range(n)]) for i in range(n)]
mincol = [min([M[j][i] for j in range(n)]) for i in range(n)]
for i in range(n):
    for j in range(n):
        if (M[i][j] == maxrow[i] == mincol[j] or
        M[i][j] == minrow[i] == maxcol[j]):
            print("(", i, j,") = ", M[i][j])