# The columns changing in the matrice
n, m = int(input()), int(input())   # A matrice space announce
M = []                              # An empty matrice
for k in range(n):                  # Iteration for rows in n
    val = [int(x) for x in input().split()]   # Filling every row in numbers as its elements
    M.append(val)                   # Creation the matrice
x, y = [int(i) for i in input().split()]   # Creation two coordinates in x and y
for i in range(n):                  # Iteration on the matrice
    M[i][x], M[i][y] = M[i][y], M[i][x]    # Value excahnges x and y

for q in range(n):   # Iteration for print
    print(*M[q])     # Output the matrice
