# Filling the matrice in the first and the third quarters in 1

n = int(input())   # Creation a size of a matrice
M = []             # An empty matrice creation
for _ in range(n): # Iteration on rows
    val = [0 for c in range(n)]   # Filling in the nulls of the each element of matrice
    M.append(val)   # Creation the full matrice

for i in range(n):  # Iteration on the matrice row
    for q in range(n):   # Iteration on the elements of the matrice
        if i <= q and i <= n - 1 - q:   # Checking the first quarter -->
            M[i][q] = 1                 # If it's true --> filling in the 1
        elif i >= q and i >= n - 1 - q: # Checking the third quarter -->
            M[i][q] = 1                 # If it's true --> filling in the 1

for i in range(n):   # Iteration on the rows
    for q in range(n):   # Iteration on the elements
        print(str(M[i][q]).ljust(3), end=" ")   # Output the result of program working
    print()                                     # The print function using fo correct view
