# The chessboard in a matrice
x = input().split()   # Two numbers inputing and transforming in a list
n, m = int(x[0]), int(x[1])  # Initialization two variables as rows and columns amount
M = []   # An empty matrice creation
for _ in range(n):   # Iteration on the rows
    val = [int(c) for c in range(m)]   # Iteration on columns 
    M.append(val)   # Creation the full matrice

for i in range(n):   # Iteration on the rows
    for j in range(m):   # Iteration on the elements in each row inside
        if (i + j) % 2 == 0:   # The condition to fill in dots
            M[i][j] = "."
        else:
            M[i][j] = "*"   # The other condiditon to fill in asterisks
            
for i in range(n):   # Iteration the matrice on the rows
    print(*M[i])     # Output the matrice on the rows 
