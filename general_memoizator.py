def square(num):
    return num * num


num = int(input())
print(square(num))


L = []
def memsquare(num):
    global L
    if len(L) <= num:
        L = L + [-1] * (num + 1)
    if L[num] == -1:
        L[num] = num * num
    return L[num]

num = int(input())
print(memsquare(num))