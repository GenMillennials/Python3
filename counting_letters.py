s = input()
counter = 0
stc = ""
for i in range(len(s)):
    if s.count(s[i]) >= counter:
        counter = s.count(s[i])
        stc = s[i]
print(stc)