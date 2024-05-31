# Every n-th element is divided on the list
x = input().split()   # Parsing the elements to transform them into a list
n = int(input())      # Creating a size of matrice
s = [[] * n for _ in range(n)]  # Creation a full matrice

for i in range(n):   # Iteration on the external loop in rows
    for j in range(i, len(x), n):   # Iteration on the nested loop
        s[i].append(x[j])   # Creation a new matrice 
print(s)                    # Output the matrice
