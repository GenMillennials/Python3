import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%,.&*+-=?\'<>\/~@^_"
chars = ""

amount = int(input("Enter the general password amount: "))
lenght = int(input("Enter the lenght of a password: "))

dig_ins = input("Is it necessary to exclude digits in a password? y / n").lower()
if dig_ins == "y" or dig_ins == "yes":

low_ins = input("Is it necessary to exclude lowercase letters in a password? y / n").lower()
if low_ins == "y" or low_ins == "yes":
    pass
else:
    pass

upp_ins = input("Is it necessary to exclude uppercase letters in a password? y / n").lower()
if upp_ins == "y" or upp_ins == "yes":
    pass
else:
    pass

punct_ins = input("Is it necessary to exclude punctuation signs in a password? y / n").lower()
if punct_ins == "y" or punct_ins == "yes":
    pass
else:
    pass

exclude = input("Exclude similar signs and letters? y / n").lower()
if exclude == "y" or exclude == "yes":
    pass
else:
    pass

chars = digits + lowercase_letters + uppercase_letters + punctuation

def generate_password(length, chars):
    L = list(chars)
    Res = list()
    while counter != 0:
        counter = length
        passw = random.choice(L)
        counter -= lenght
