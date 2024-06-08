# Filling the digits in the secondary matrice diagonal
n = int(input())   # Input a size of a square matrice
M = []             # An empty matrice creation
for _ in range(n): # Iteration on the rows
    val = [int(x) for x in range(n)]  # Iteration on the elements of matrice
    M.append(val)  # Creation the full matrice
    
for i in range(n):  # Iteration on the rows
    for q in range(n):  # Itereation on the elements
        if i == n - 1 - q:   # Filling in 1 if the main and the secondary diagonal is equality
            M[i][q] = 1
        elif i < n - 1 - q:   # Filling in 0 if the main diagonal less than the secondary diagonal
            M[i][q] = 0
        elif i > n - 1 - q:   # Fillng in 2 if the main diagonal more than the secondary diagonal
            M[i][q] = 2

for i in range(n):   # Iteration on the matrice rows
    print(*M[i])     # Output the result in rows
