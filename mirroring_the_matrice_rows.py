# The mirroring rows in the matrice
n = int(input())   # Announce a deepth of a matrice
M = []             # An empty matrice creation
for _ in range(n):   # Iteration on the matrice deepth
    val = [int(x) for x in input().split()]   # Filling each iteratoin in numbers
    M.append(val)   # Creation the full matrice
    
for i in range(n - 1, -1, -1): # Output the matrice rows from the bottom to the high with iteration conditions
    print(*M[i])   # Output the matrice in rows without the list datatype