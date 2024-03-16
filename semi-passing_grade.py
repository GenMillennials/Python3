n = int(input("Enter the applicants amount: "))
m = int(input("Enter the college free position: "))
A = int(input("Maximal score is: "))
L = [0] * (A + 1)
print("Scores:")
for i in range(n):
    a = int(input())
    L[a] = L[a] + 1
s = 0
for i in range(1, A):
    s = s + L[-i]
    if s > m:
        print("The amount of the semi-passing grade applicants are: ", L[-i])
        break
    elif s == m:
        print("The amount of the semi-passing grade applicants are: ", 0)
        break   