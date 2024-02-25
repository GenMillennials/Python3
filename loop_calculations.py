n = int(input())
cntr_3 = 0
cntr_ld = 0
cntr_even = 0
sum_5 = 0
mult_7 = 1
cntr_0_5 = 0
ld = n % 10
while n != 0:
    if n % 10 == 3:
        cntr_3 += 1
    if ld == n % 10:
        cntr_ld += 1
    if n % 10 % 2 == 0:
        cntr_even += 1
    if n % 10 > 5:
        sum_5 += n % 10
    if n % 10 > 7:
        mult_7 *= n % 10
    if n % 10 == 0 or n % 10 == 5:
        cntr_0_5 += 1
    n //= 10
print(cntr_3, cntr_ld, cntr_even, sum_5, mult_7, cntr_0_5, sep="\n")