s = input().upper()
phone_keyboard = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "
}

for i in s:
    for key, value in phone_keyboard.items():
        if i in value:
            print(key * (value.index(i) + 1), end="")
            