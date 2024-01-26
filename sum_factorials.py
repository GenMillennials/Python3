""" def fact(num):
    p=1
    for i in range(1,num+1):
        p=p*num
    return p

def sigma(num,func):
    s=0
    for i in range(1,num+1):
        s=s+func(i)
    return s

num=int(input())
print(sigma(num,fact)) """


from functools import reduce

n = int(input())
L = list(range(1, n+1))
func = reduce(lambda a, b: a * b, L)
print(func)