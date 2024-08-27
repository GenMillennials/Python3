import random

L = [input() for _ in range(int(input()))] # Enter the amount and the personnel names
random.shuffle(L)
for i in range(len(L)):
    print(f"{L[i-1]} - {L[i]}")
