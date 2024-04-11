ID = input()
flag = False
ABC = "АВЕКМНОРСТУХ"
if len(ID) == 9 or len(ID) == 10:
    lets = ID[0] + ID[4:6]
    nums = ID[1:4] + ID[7:]
    sym = ID[6]
    if nums.isdigit() and sym == "_":
        flag = True
    for i in lets:
        if i not in ABC:
            flag = False
            break
print("YES" if flag == True else "NO")
