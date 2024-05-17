# Searching maximal digit on and under the main matrice digonal
n = int(input())   # The Rows amount number in matrice
M = []             # An empty matrice announce
for i in range(n):   # Loop for n iteration
    val = [int(k) for k in input().split()]   # Pouring the marice rows with elements
    M.append(val)    # Creating the full matrice

Max = M[0][0]   # Starting position to maximal point checking
for k in range(n):   # The first iteration on matrice to rows
    for q in range(n):   # The nested loop iteration on matrice to elements
        if k >= q and M[k][q] > Max:   # If element above the main diagonal and the current element more than Max value -->
            Max = M[k][q]   # --> The Max value updates
print(Max)   # Output the maximal value above the main matrice diagonal