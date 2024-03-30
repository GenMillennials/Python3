import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%,.&*+-=?\'<>\/~@^_"
chars = ""

amount = int(input("Enter the general password amount: "))
lenght = int(input("Enter the lenght of a password: "))

chars = digits + lowercase_letters + uppercase_letters + punctuation

while amount > 0:
    def generate_password(length, chars):
        L = list(chars)
        Res = list()
        for i in range(lenght):
            i = random.choice(L)
            Res.append(i)
            password = "".join(Res)
        return password
    amount -= 1

print(generate_password(lenght, chars))
