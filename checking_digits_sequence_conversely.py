n = int(input())
f = True
counter = 0
while n > 0:
    last_d = n % 10
    if last_d >= counter:
        f = True
        counter = last_d
    else:
        f = False
        break
    n //= 10
if f:
    print("Yes")
else:
    print("No")