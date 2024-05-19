# Times table in the matrice
n, m = int(input()), int(input())   # Input two int variables for numbers
M = list()                          # Creation am empty matrice
for k in range(n):                  # Initiation the external loop
    val = [x for x in range(m)]     # Initiaton the elements in the nested loop
    M.append(val)                   # Creation the matrice
    
for i in range(n):                  # Creation the first number for the times table from 0
    for q in range(m):              # Iteration the second number for the times table from 0
        M[i][q] = i * q             # Multiplication to store in M[i][q] variable
    
for i in range(n):                  # The external loop for output the matrice
    for q in range(m):              # The nested loop for output the matrice
        print(str(M[i][q]).ljust(3), end=" ")   # Outpur the result with lining to the left side in string
    print()                         # End the printed string
    