# Filling matrice in both the main and the secondary diagonals with 1

n = int(input())   # Creation a size of a matrice
M = []             # An empty matrice creation
for _ in range(n): # Iteration on rows
    val = [0 for c in range(n)]   # Filling in null all elements
    M.append(val)  # Creation the full matrice with nulls filled

for i in range(n):   # Iteration on the each row in the matrice
    for j in range(n):   # Iteration on the elements in the nested loop
        if i == j:   # If the main diagonal index equals the index of element -->
            M[i][j] = 1   # --> Filling it in the 1
        elif i == n - 1 - j:   # If the row element equals the secondary diagonal element -->
            M[i][j] = 1   # --> Filling it in the 1

for i in range(n):   # Iteration on the rows
    print(*M[i])     # Output the matrice table
