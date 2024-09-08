from fractions import Fraction as F
a, b = input(), input()

print(a, '+', b, '=', F(a)+F(b))
print(a, '-', b, '=', F(a)-F(b))
print(a, '*', b, '=', F(a)*F(b))
print(a, '/', b, '=', F(a)/F(b))