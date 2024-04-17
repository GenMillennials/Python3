def is_decryption(d):
    L = list()
    s = str()
    for j in range(26):
        for i in d:
            if i.isupper():
                s = chr((((ord(i) - 65) - j) % 26) + 65)
                L.append(s)
            elif i.islower():
                s = chr((((ord(i) - 97) - j) % 26) + 97)
                L.append(s)
            else:
                s = i
                L.append(s)
    return "".join(L)

print("Welcome to encoding Caesar encryption!")
data = input("Input the encrypted text in English: ")
res = is_decryption(data).split(".")
for i in res:
    m = i + "."
    print(m)
