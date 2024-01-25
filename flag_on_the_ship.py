""" T = [int(el) for el in input().split()]
c = 0
for t in T:
    if t > 37:
        c = c + 1
if c > 0:
    print("Someone got sick")
else:
    print("All passengers are healthy") """


""" T = [int(el) for el in input().split()]
c = sum(t > 37 for t in T)
if c > 0:
    print("Someone got sick")
else:
    print("All passengers are healthy") """