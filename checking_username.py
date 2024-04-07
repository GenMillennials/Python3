username = input()
flag1, flag2, flag3 = True, True, True
if username[0] != "@":
    flag1 = False
if len(username) < 5 or len(username) > 15:
    flag2 = False
for i in username[1::]:
    if not (i.isalnum() and (i.islower() or i.isdigit())):
        flag3 = False
print("Correct" if flag1 == True and flag2 == True and flag3 == True else "Incorrect")