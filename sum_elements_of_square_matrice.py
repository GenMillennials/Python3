# The sum of elements in the main diagonal
n = int(input())   # Initiation rows and columns in a square matrice
M = []             # Initiation an empty matrice object
counter = 0        # Initiation the counter for the sum of the main matrice diagonal
for k in range(n):   # Iteration to create the square matrice
    val = [int(t) for t in input().split()]   # Writing down the matrice in row digits with spaces
    M.append(val)   # Adding list modules into the matrice
    
for i in range(n):   # Iteration on existing matrice elements
    counter += M[i][i]   # Getting each element of matrice and adiing them to the counter varible
print(counter)       # Output the counter variable