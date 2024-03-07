n = input().split("-")
t = [len(i) for i in n]
if t == [3, 3, 4] and "".join(n).isdigit():
    print("YES")
elif t == [1, 3, 3, 4] and "".join(n).isdigit() and t[0] == "7":
    print("YES")
else:
    print("NO")