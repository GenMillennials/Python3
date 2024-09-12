from math import gcd
from fractions import Fraction as F

n = int(input())
result = []
while n != 1:
    for i in range(1, n):
        if gcd(i, n) == 1:
            result.append(f'{i}/{n}')
    n -= 1
answer = sorted(map(F, result))
print(*answer, sep='\n')
