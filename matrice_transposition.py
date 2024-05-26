# The matrice transposition
n = int(input())   # Announcing a deepth of matrice by a numnber
M = []             # An empty matrice announce
for _ in range(n):   # Iteration on rows
    val = [int(x) for x in input().split()]   # Filling the elements in the matrice
    M.append(val)   # The full matirce generation

for i in range(n):   # The external loop for each matrice row
    for j in range(n):   # The nested loop to iterate matrice elements in the row
        print(M[j][i], end=" ")   # Output the matrice which changing rows to elements and elements to rows
    print()              # The print function to correct output the matrice
