n = int(input("Enter the applicants amount: "))
m = int(input("Enter the college free position: "))
L = [-1] * m
cntr = 0
print("Scores:")
for i in range(n):
    a = int(input())
    for j in range(m):
        if a >= L[j]:
            L.insert(j, a)
            if L[-1] == L[-2]:
                cntr += 1
            else:
                cntr = 0
            L = L[:-1]
            break
if cntr != 0:
    cntr = cntr + L.count(L[-1])
print("The amount of the semi-passing grade applicants are: ", cntr)
   