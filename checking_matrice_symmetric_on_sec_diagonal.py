# Checkin the symmetrics of the matrice through its secondary diagonal
# We could check the symmetrics as Matrice[i][j] == Matrice[n-j-1][n-j-1]
n = int(input())   # Creation a size of a square matrice
M = []             # An empty matrice creation
flag = True        # Creation a flag on True condition by default
for _ in range(n): # Iteration the rows of the matrice for its filling
    val = [int(x) for x in input().split()]   # Filling the matice elements on the rows in numbers
    M.append(val)  # Creation the full filling matrice
M.reverse()        # Reversing the created matrice

for i in range(n):   # The external loop to iterate the matrice rows
    for q in range(n):   # The nested loop to iterate the matrice elements
        if M[i][q] != M[q][i] and i != q:   # Checking the symmetric on the both diagonals -->
            flag = False # If its no symmetric --> Flag on False
            break        # --> Exit of the loop
if flag:                 # If Flag turns out on True -->
    print("YES")         # --> Output "YES"
else:                    # If Flaf on False -->
    print("NO")          # --> Output "False"
