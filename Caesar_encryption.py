def welcome():
    print("Welcome to Caesar's encryption and decryption generator!")

def enter_data():
    print("Enter your text:")
    data = input()
    return data   # str()

def rotate():
    shift = int(input("Enter the rotate index: "))
    return shift   # int()

def is_encryption_eng(data, rotate):
    L = list()
    s = str()
    for i in data:
        if i.isupper():
            s = chr((((ord(i) - 65) + rotate) % 26) + 65)
            L.append(s)
        elif i.islower():
            s = chr((((ord(i) - 97) + rotate) % 26) + 97)
            L.append(s)
        else:
            s = i
            L.append(s)
    return "".join(L)   # str()

def is_encryption_rus(data, rotate):
    L = list()
    s = str()
    for i in data:
        if s.isupper():
            s = chr((((ord(i) - 1040) + rotate) % 32) + 1040)
            L.append(s)
        if s.islower():
            s = chr((((ord(i) - 1072) + rotate) % 32) + 1072)
            L.append(s)
        else:
            s = i
            L.append(s)
    return "".join(L)   # str()

def is_decryption_eng(data, rotate):
    L = list()
    s = str()
    for i in data:
        if i.isupper():
            s = chr((((ord(i) - 65) - rotate) % 26) + 65)
            L.append(s)
        elif i.islower():
            s = chr((((ord(i) - 97) - rotate) % 26) + 97)
            L.append(s)
        else:
            s = i
            L.append(s)
    return "".join(L)   # str()

def is_decryption_rus(data, rotate):
    L = list()
    s = str()
    for i in data:
        if i.isupper():
            s = chr((((ord(i) - 1040) - rotate) % 32) + 1040)
            L.append(s)
        elif i.islower():
            s = chr((((ord(i) - 1072) - rotate) % 32) + 1072)
            L.append(s)
        else:
            s = i
            L.append(s)
    return "".join(L)   # str()

welcome()
action = input("Would you like to encrypt of decript your data? encr / decr ").lower()
lang = input("Pick the language: eng / rus ").lower()
if (lang == "eng" or lang == "e" or lang == "en" or lang == "english") and (action == "encr" or action == "e" or action == "enc" or action == "en" or action == "encryption"):
    print(is_encryption_eng(enter_data(), rotate()))
elif (lang == "rus" or lang == "r" or lang == "ru" or lang == "russian") and (action == "encr" or action == "e" or action == "enc" or action == "en" or action == "encryption"):
    print(is_encryption_rus(enter_data(), rotate()))
elif (lang == "eng" or lang == "e" or lang == "en" or lang == "english") and (action == "decr" or action == "de" or action == "dec" or action == "de" or action == "d" or action == "decryption"):
    print(is_decryption_eng(enter_data(),rotate()))
elif (lang == "rus" or lang == "r" or lang == "ru" or lang == "russian") and (action == "decr" or action == "de" or action == "dec" or action == "de" or action == "d" or action == "decryption"):
    print(is_decryption_rus(enter_data(),rotate()))