s = input().split()  # Enter the text in English
counter = 0
for i in s:
    if i.lower() == "a" or i.lower() == "an" or i.lower() == "the":
        counter += 1
print("The total numbers of articles:", counter)