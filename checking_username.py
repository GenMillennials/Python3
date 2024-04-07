username = input()
flag1, flag2, flag3 = True, True, True
if username[0] != "@":
    flag1 = False
if len(username) < 5 or len(username) > 15:
    flag2 = False
for i in username[1::]:
    if i == i.isalnum():
        flag3 = True
if username[1::].islower():
    flag3 = True
else:
    flag3 = False
print("Correct" if flag1 == True and flag2 == True and flag3 == True else "Incorrect")
