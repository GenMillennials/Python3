# Filling matrice in the numbers 0, 1, 2
x = input().split()   # Input two numbers for a size of a matrice
n, m = int(x[0]), int(x[1])   # Creation the lenght and the hight of the matrice
M = []                # The empty matrice creation
for _ in range(n):    # Iteration the rows on the matrice
    val = [c for c in range(m)]   # Iteration the elements on the matrice
    M.append(val)     # Creation the full matrice

count = 1             # Creation a counter in 1 value by default
for i in range(n):    # Itereation on the rows
    for j in range(m):   # Itereation on the each element of the matrice
        M[i][j] = count  # Every element of the matrice is attaching 1
        count += 1       # And every iteration the count increase on 1
        
for i in range(n):       # Iteration on the rows
    for j in range(m):   # Iteration on the elements
        print(str(M[i][j]).ljust(3), end=" ")   # Output in the ljust() method for the right view
    print()                                     # The technical call of the print function
