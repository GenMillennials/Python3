# Filling the matrice in numbers through diagonals
x = input().split()   # Filling two numbers in the list
n, m = int(x[0]), int(x[1])   # Override that nubers into n and m values
M = []                # An empty matrice creation
for _ in range(n):    # Itreration the matrice rows
    val = [k for k in range(m)]   # Creation the elements in the matrice rows
    M.append(val)                 # Creation the full matrice

count = 1                         # The counter switch on 1
for i in range(n * m):            # Iteration the full indices of the matrice
    for j in range(n):            # Iteration in rows
        for q in range(m):        # Iteration in elements
            if j + q == i:        # Checking every element to match i that point to the matrice diagonal
                M[j][q] = count   # Adding the element value in the count
                count += 1        # Adding the count to 1

for i in range(n):
    for j in range(m):
        print(str(M[i][j]).ljust(3), end=" ")   # Output the matrice
    print()