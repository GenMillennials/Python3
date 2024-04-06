def welcome():
    print("Welcome to Caesar's encryption and decryption generator!")

def is_action():
    action = input("Would you like to encrypt of decript your data? encr / decr ").lower()
    # if action == "encr" or action == "enc" or action == "en" or action == "e" or action == "encryption":
    #     is_encryption = action
    # elif action == "decr" or action == "dec" or action == "de" or action == "d" or action == "decryption":
    #     is_decryption = action
    return action

def pick_lang():
    eng_lang = "abcdefghijklnopqrstuvwxyz"
    rus_lang = "абвгдежзиклмнопрстуфхцчшщъыьэюя"
    lang = input("Pick the language: eng / rus ").lower()
    if lang == "eng" or lang == "e" or lang == "en" or lang == "english":
        lang = eng_lang
    if lang == "rus" or lang == "r" or lang == "ru" or lang == "russian":
        lang = rus_lang
    return lang   # str()

def enter_data():
    print("Enter your text for encryption or decryption:")
    data = input()
    return data   # str()

def rotate():
    shift = int(input("Enter the rotate index: "))
    return shift   # int()

def is_encryption(data, rotate):
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

def is_decryption(data, rotate):
    L = list()
    s = str()
    for i in data:
        if i.isupper():
            s

welcome()
#is_action()
#pick_lang()
#enter_data()
#rotate()