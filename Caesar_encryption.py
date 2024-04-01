print("Welcome to Caesar's encryption and decryption generator!")
action = input("Would you like to encrypt of decript your data? encr / decr").lower()
if action == "encr" or action == "enc" or action == "en" or action == "e":
    pass
elif action == "decr" or action == "dec" or action == "de" or action == "d":
    pass
lang = input("Pick the language: eng / rus").lower()
eng_lang = "abcdefghijklnopqrstuvwxyz"
rus_lang = "абвгдежзиклмнопрстуфхцчшщъыьэюя"
rotate = int(input("Pick the rotate index: "))
print("Enter your text for encryption or decryption:")
data = input()
print(data)

def encryption(data):
    L = [data]
    if lang == "eng" or lang == "e" or lang == "english":
        pass
    if lang == "rus" or lang == "r" or lang == "russian":
        pass

def decryption(data):
    pass