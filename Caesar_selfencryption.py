w = input()
s = w
for i in s:
    if i in "@,.!?:\'\"*-;":
        s = s.replace(i, "")
x = [len(j) for j in s.split()]
cnt = 0
word = ""
for k in w:
    num = ord(k)
    if k == " ":
        cnt += 1
        word += k
    elif 65 <= num <= 90:
        if num + x[cnt] > 90:
            word += chr(num + x[cnt] - 26)
        else:
            word += chr(num + x[cnt])
    elif 97 <= num <= 122:
        if num + x[cnt] > 122:
            word += chr(num + x[cnt] - 26)
        else:
            word += chr(num + x[cnt])
    else:
        word += k
print(word)