s1 = sorted(input())
s2 = sorted(input())

dict1 = dict(zip(range(len(s1)), s1))
dict2 = dict(zip(range(len(s2)), s2))

if dict1 == dict2:
    print("YES")
else:
    print("NO")

