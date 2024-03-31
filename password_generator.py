import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%,.&*+-=?\'<>\/~@^_"
chars = ""

amount = int(input("Enter the general password amount: "))
length = int(input("Enter the length of a password: "))
digits_c = input("Is it necessary to include digits in the password? y / n: ").lower()
lowercase_letters_c = input("Is it necessary to include lowercase letters in the password? y / n: ").lower()
uppercase_letters_c = input("Is it necessary to include uppercase letters in the password? y / n: ").lower()
punctuation_c = input("Is it necessary to include punctuation symbols in the password? y / n: ").lower()

def get_chars():
    L = []
    if digits_c == "y" or digits_c == "yes":
        L.append(digits)
    if lowercase_letters_c == "y" or lowercase_letters_c == "yes":
        L.append(lowercase_letters)
    if uppercase_letters_c == "y" or uppercase_letters_c == "yes":
        L.append(uppercase_letters)
    if punctuation_c == "y" or punctuation_c == "yes":
        L.append(punctuation)
    return "".join(L)   # str

def generate_single_password(get_chars):
    L = list(get_chars)
    password = str()
    for _ in range(length):
        symbs = random.choice(L)
        password += symbs
    return password   # str()

passwords = list()
while amount > 0:
    passwords.append(generate_single_password(get_chars()))   # list()
    amount -= 1

print(*passwords, sep="\n")