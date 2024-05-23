# The matrice diagonals exchange
n = int(input())   # Entered a matrice deepth
M = []             # An empyty matrice annotation
for _ in range(n):   # Iteration on the matcice deepth as its rows
    val = [int(x) for x in input().split()]   # Input the elements in the every row
    M.append(val)   # Establishing the full matrice filling

for i in range(n):   # Iteration the matrice rows
    M[i][i], M[n - 1 - i][i] = M[n - 1 - i][i], M[i][i]   # Both diagonals exchanges inside the matrice

for q in range(n):   # Iteration the matrice rows to ounput it
    print(*M[q])     # Output the result of changing the matrice diagonals
    