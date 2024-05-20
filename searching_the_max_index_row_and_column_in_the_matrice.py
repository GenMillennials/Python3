# The row and the column index position with the maximal matrice element
n, m = int(input()), int(input())  # Definition rows and columns amount
M = []                             # An empty matrice 
for k in range(n):                 # Iteration rows amount
    val = [int(x) for x in input().split()]   # Filling the numbers in the rows
    M.append(val)                  # Creation the full matrice
x = 0                              # The intiation an index for the row
y = 0                              # The initiantion an index for the column
M_max = M[0][0]                    # The first start value of the matrice by default
for i in range(n):                 # The external loop to iterate the matrice
    for j in range(m):             # The nested loop to iterate the matrice
        if M[i][j] > M_max:        # Checking every value in the matrice  -->
            M_max = M[i][j]        #  --> Overriding variable if True
            x = i                  # Changing x variable
            y = j                  # Changing y variable
print(x, y)                        # Output x and y variables
