def Standard_American_Convention(num: int):
    a = str(num)
    if len(a) <= 3:
        return a
    else:
        L = list()
        while len(a) > 3:
            L.append(a[-3:])
            a = a[:-3]
        L.append(a)
    return ",".join(reversed(L))

        
n = int(input())
print(Standard_American_Convention(n))