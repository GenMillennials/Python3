# Filling the matrice the different number row sequences
x = input().split()   # Input two numbers
n, m = int(x[0]), int(x[1])   # Creation the height and the width of a matrice
val = [i for i in range(1, m + 1)]   # Creation the sequence of numbers
M = []                        # An empty matrice creation

for i in range(n):   # Iteration on the row
    M.append(val)    # Adding the created sequence
    val = val[1:] + [val[0]]   # Substitution the end element in the each row in iteration

for i in range(n):   # Iteration on the row
    for j in range(m):   # Iteration on the elements
        print(str(M[i][j]).ljust(3), end=" ")   # Output the lined elements 
    print()                                     # The print function for correct matrice output
