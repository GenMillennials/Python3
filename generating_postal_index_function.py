import random
import string

def generate_index():
    upper_letter = string.ascii_uppercase
    s1, s2, s3, s4 = (random.choice(upper_letter) for i in range(4))
    number1, number2 = (random.randint(0, 99) for i in range(2))
    return f"{s1}{s2}{number1}_{number2}{s3}{s4}"

print(generate_index())