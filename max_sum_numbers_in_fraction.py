from fractions import Fraction as F

n = int(input())
L = list()
for i in range(1, n - 1):
    for j in range(i + 1, n):
        k = F(i, j)
        if k.numerator + k.denominator == n:
            L.append(k)
print(max(L))
