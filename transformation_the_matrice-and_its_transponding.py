# Transformation strings in the matrix and its transponding 
n, m = int(input()), int(input())   # Enter matrice rows and columns general amount
M = []                              # Creating an empty list for a matrice storage
for _ in range(n):                  # Start the external itteration to each matrice row
    row = []                        # Initiating an empty row list for further value accumulation
    for __ in range(m):             # Start the nested loop for columns in the matrice
        row.append(input())         # Appending all entered string values into columns and dividing they to rows
    M.append(row)                   # Creating the matrice with the rows
                                    # Matrice OUTPUT
for k in range(n):                  # Creating the external loop for a row amount iteration
    for l in range(m):              # Creating the nested loop for a column amount iteration
        print(M[k][l], end=" ")     # Matrice output the each column in row position by indices
    print()                         # Formatting print function for the matrice

print()                             # Creating a space between the second output
                                    # TRANSPONDING Matrice output
for i in range(m):                  # Creating the external loop for the column amount iteration
    for j in range(n):              # Creating the external loop for the row amount iteration
        print(M[j][i], end=" ")     # Transponded matrice output
    print()                         # Formatting print function for the matrice