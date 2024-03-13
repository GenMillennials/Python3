n = int(input("Enter the applicants amount: "))
m = int(input("Enter the college free position: "))
print(f"Enter the points of each applicant ({n})")
c = 1
for i in range(n):
    a = int(input())
    if i > 1:
        if a == ap:
            c = c + 1
        else:
            if i > m:
                break
            elif i == m:
                c = 0
                break
            c = 1
    ap = a
print("The semi-passing grade applicants are: ", c)

