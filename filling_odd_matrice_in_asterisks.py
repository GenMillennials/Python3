# Filling the matrice in asterisks by odd n-index (for //)
n = int(input())   # Creation a size of matrice variable
M = []             # An empty matrice announcing
for _ in range(n): # Iteration the size of matrice
    val = ["." for t in range(n)]   # Filling every matrice element in a dot
    M.append(val)  # Creation the full matrice by dots

for i in range(n):   # The external loop to iterate the matrice rows
    for j in range(n):   # The nested loop to iterate its elements
        if i == j or i == n - 1- j:   # Filling the main and the second diagonals of the matrice in asterisks 
            M[i][j] = "*"             #  ^^^   ^^^   ^^^
        elif n // 2 == i or n // 2 == j:   # Filling the optional matrice elements in asteresks
            M[i][j] = "*"                  #  ^^^   ^^^   ^^^
        
for i in range(n):   # Iteratoin the size of matrice
    print(*M[i])     # Output the signs of the matrice
    