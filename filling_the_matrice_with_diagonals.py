# Filling the matrice in numbers with diagonals
n = int(input())   # Creation a size of matrice 
M = []             # An empty matrice creation
for _ in range(n): # Iteration on matrice rows
    val = [0 for k in range(n)]   # Filling the elements of matrice in nulls
    M.append(val)  # Creation the full matrice by nulls

for i in range(n):   # The external loop to iterate on the matrice rows
    for j in range(n):   # The nested loop to iterate on the matrice elements inside the each row
        if j > i:        # Checking the content of the matrice for I and II quarters, if it's True condition -->
            M[i][j] = j - i   # --> difference between the column index and the row index for I and II quarters
        elif i > j:      # Checking the content of the matrice for III and IV qurters, if it's True condition -->
            M[i][j] = i - j   # difference between the row index and the column index for III and IV quarters
        
for i in range(n):   # Iteration on the matrice rows
    print(*M[i])     # Output the result of the programm
