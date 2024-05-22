# Symmetric matrice checking
n = int(input())   # Entered the size of a matrice
M = []             # An empty matrice announcing
flag = True        # Creation a flag for symmetric indication 
for _ in range(n):   # Iteration loop for n
    val = [int(x) for x in input().split()]   # Creation the filling to the matrice
    M.append(val)   # Creation the full matrice

for i in range(n):   # Iteration for rows of the matrcie
    for q in range(n):   # Iteration for elements in the each row
        if M[i][q] != M[q][i] and i != q:   # Checking opposite elements for asymmetric --> if it's the True confition -->
            flag = False   # --> False flag switch on
            break          # breaking the loop
if flag:                   # If flag is True -->
    print("YES")           # Yes ouput
else:                      # Is flag turned out False
    print("NO")            # No output