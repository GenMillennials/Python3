n = int(input("Enter the applicants amount: "))
m = int(input("Enter the college free position: "))
print(f"Enter the points of each applicant ({n})")
a = list()
for i in range(n):
    a.append(int(input()))
if a[m] != a[m - 1]:
    print("The semi-passing grade applicants are: ", a.count(a[m]))
else:
    print("The semi-passing grade applicants is ", 0)

