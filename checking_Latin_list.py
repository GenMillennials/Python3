# The Latin square checking in the matrice
n = int(input())   # Creation the size of matrice
flag = True        # Creation a flag on true by default
M = []             # An empty matrice announce
for _ in range(n): # Iteration the rows in the matrice
    val = [int(x) for x in input().split()]   # Filling the matrice in elements into each row
    M.append(val)  # Creation the full matrice
    
lat_list = [i for i in range(1, n + 1)]       # Forming the Latin list with list comprehension
for i in range(n):                            # Iteration the external list
    x = sorted(M[i])                          # Sorting the elements in every row with interation
    y = sorted([M[j][i] for j in range(n)])   # Sorting the elements in every column with iteration
    if x != lat_list or y != lat_list:        # Checking to match x and y position on the Latin list --> if it's True -->
        flag = False                          # The flag changes on False

if flag:                                      # If flag on True
    print("YES")                              # Output "YES"
else:                                         # If flag on False
    print("NO")                               # Output "NO"
    