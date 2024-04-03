print("Welcome to Caesar's encryption and decryption generator!")
action = input("Would you like to encrypt of decript your data? encr / decr").lower()
lang = input("Pick the language: eng / rus").lower()
eng_lang = "abcdefghijklnopqrstuvwxyz"
rus_lang = "абвгдежзиклмнопрстуфхцчшщъыьэюя"
rotate = int(input("Pick the rotate index: "))
print("Enter your text for encryption or decryption:")
data = input()

def pick_action_lang():
    global action
    if action == "encr" or action == "enc" or action == "en" or action == "e":
        action = is_encryption
    elif action == "decr" or action == "dec" or action == "de" or action == "d":
        action = is_decryption
    return action   # 

def pick_lang():
    global eng_lang, rus_lang
    if lang == "eng" or lang == "e" or lang == "en" or lang == "english":
        eng_lang = lang
    if lang == "rus" or lang == "r" or lang == "ru" or lang == "russian":
        rus_lang = lang
    return lang   # str()

def is_encryption(data, rotate):
    L = list(data)
    for i in L:
        if i.isupper():
            s = # range(65, 91)
        else:
            s = chr(ord(i) + rotate)

def is_decryption(data, rotate):
    pass