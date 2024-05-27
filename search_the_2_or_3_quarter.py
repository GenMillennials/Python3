# Search the max element in the 2 and 3 quarters and the second matrice daigonal include
n = int(input())   # Creation a deepth of matrice
M = []             # An empty matrice creation
for _ in range(n): # The external loop n for rows creating
    val = [int(x) for x in input().split()]   # Filling every row in numbers
    M.append(val)   # The full matrice creation

Max = M[0][0]   # Initialization the first element of matrice in [0][0] position
for i in range(n):   # The external loop for rows iteration
    for j in range(n):   # The nested loop for elements iteration
        if i >= n - 1 - j and M[i][j] > Max:   # If row in 2 or 3 quarters and maximal element more than previous value -->
            Max = M[i][j]   # The maximal element override to the new value
print(Max)   # Output the maximal value in the 2 and 3 matrice quarters