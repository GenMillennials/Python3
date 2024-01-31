""" def memo(func):
    L = []
    def result(num):
        nonlocal L
        if num >= len(L):
            L = L + [-1] * (num + 1)
        if L[num] == -1:
            L[num] = func(num)
        return L[num]
    return result


def fibonacci(num):
    if num <= 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


memfibonacci = memo(fibonacci)
num = int(input())
print(memfibonacci(num)) """




def memo(func):
    L = []
    def result(num):
        nonlocal L
        if num >= len(L):
            L = L + [-1] * (num + 1)
        if L[num] == -1:
            L[num] = func(num)
        return L[num]
    return result


@memo
def fibonacci(num):
    if num <= 2:
         return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


num = int(input())
print(fibonacci(num))