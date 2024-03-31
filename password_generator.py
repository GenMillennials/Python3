import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%,.&*+-=?\'<>\/~@^_"
chars = ""

amount = int(input("Enter the general password amount: "))
length = int(input("Enter the length of a password: "))

chars = digits + lowercase_letters + uppercase_letters + punctuation

def generate_single_password():
    L = list(chars)
    password = str()
    for _ in range(length):
        symbs = random.choice(L)
        password += symbs
    return password

passwords = list()
while amount > 0:
    passwords.append(generate_single_password())
    amount -= 1

print(*passwords, sep="\n")