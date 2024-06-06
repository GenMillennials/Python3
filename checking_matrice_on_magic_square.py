# Checking matrice as a magic square
n = int(input())
M = []
for _ in range(n):
    val = [int(x) for x in input().split()]
    M.append(val)
digits = [i for i in range(1, n ** 2 + 1)]

d1, d2 = 0, 0   # counters for the main and side diagonals
for i in range(n):
    col_sum, row_sum = 0, 0
    for j in range(n):
        col_sum += M[j][i]
        row_sum += M[i][j]
        if M[i][j] in digits:
            digits.remove(M[i][j])
    d1 += M[i][i]
    d2 += M[i][n - i - 1]
    if col_sum != row_sum:
        break

if col_sum == row_sum == d1 == d2 and digits == []:
    print("YES")
else:
    print("NO")
