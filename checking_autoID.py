ID = input()
flag = True
if len(ID) != 9 and len(ID) != 10:
    flag = False
ABC = "АВЕКМНОРСТУХ"
print("NO" if flag == False else "YES")
