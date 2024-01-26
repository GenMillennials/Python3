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


""" from functools import reduce

def factorial(num):
    L = list(range(1, num + 1))
    func = reduce(lambda a, b: a * b, L)
    return func

num = int(input())
L = list(range(1, num + 1))
print(L)
M = list(map(factorial, L))  # Created a new list with the map() built-in function
print(M)
print(sum(M)) """


from functools import reduce

def factorial(num):
    return reduce(lambda a, b: a * b, range(1, num + 1))

num = int(input())
print(sum(list(map(factorial, range(1, num + 1)))))


""" from functools import reduce

num = int(input())
print(sum(list(map(lambda num: reduce(lambda a, b: a * b, range(1, num + 1)), range(1, num + 1))))) """