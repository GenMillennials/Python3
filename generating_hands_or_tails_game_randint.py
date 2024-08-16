import random
print("Input the game amount")
n = int(input())

for _ in range(n):
    number = random.randint(0, 1)
    if number == 1:
        print("Head")
    else:
        print("Tail")
