# Turning the matrice to 90 degrees to clockwise
n = int(input())   # Definition the size of squre matrice
M = []             # An empty matrice announcing
for _ in range(n):   # Iteration n for rows in the future matrice creation
    val = [int(x) for x in input().split()]   # Creation the matrice rows with numbers
    M.append(val)   # Creation the full matrice

for i in range(n):   # The external loop on the matrice
    for q in range(n - 1, -1, -1):   # The nested loop with opposite steps in elements
        print(M[q][i], end=" ")      # Output the matrice in the other order
    print()                          # The print function to fixate the matrice above
