# Calculating the sum of quarters not including the diagonals
n = int(input())   # Definition the size of a matrice
M = []             # Creatinf an empty list for matrice
for k in range(n): # Initiation a loop for n iteration
    val = [int(m) for m in input().split()]   # Writing values down in the matrice rows
    M.append(val)  # Creatiog the full matrice

Sum1 = 0   # Initiation 4 variables for the sum of each quarters
Sum2 = 0
Sum3 = 0
Sum4 = 0
for i in range(n):   # Initiation the external loop
    for j in range(n):   # Initiation the nested loop to iterate all matrice values across its rows
        if i < j and i < n - 1 - j:   # If condition to definite the precise position each element in the matrice and adding their numbers --> for the upper quarter
            Sum1 += M[i][j]           
        elif i < j and i > n - 1 - j: # --> sum for the right quarter
            Sum2 += M[i][j]     
        elif i > j and i > n - 1 - j: # --> sum for the lower quarter
            Sum3 += M[i][j]
        elif i > j and i < n - 1 - j: # --> sum for the left quarter
            Sum4 += M[i][j]
print(f"Upper quarter: {Sum1}")   # Output the numbers value for each qurater wuth f-string
print(f"Right quarter: {Sum2}")
print(f"Lower quarter: {Sum3}")
print(f"Left quarter: {Sum4}")