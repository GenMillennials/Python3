# Filling matrice in the column sequence

x = input().split()   # Input two numbers for lenght and height a matrice
n, m = int(x[0]), int(x[1])   # Distribution the numbers on the lenght and height
M = []                # An empty matrice creation
for _ in range(n):    # Itereation on the rows' matrice
    val = [c for c in range(m)]   # Filling in the elements of the matrice
    M.append(val)     # Creation the full matrice

count = 1             # Creation the counter on 1 by default
for j in range(m):    # Iteration on the rows
    for i in range(n):   # Iteration on the elements
        M[i][j] = count  # Checking the vertical columns
        count += 1       # Adding the next number to the counter
        
for i in range(n):       # Iteration on the rows
    for j in range(m):   # Iteration on the elements in the row
        print(str(M[i][j]).ljust(3), end=" ")   # Output the result in the ljust()string method processing
    print()              # The print function to correct working the matrice table output
