def binary(n):
    res = bin(n)
    print(res[2:])

def octal(n):
    res = oct(n)
    print(res[2:])

def hexidecimal(n):
    res = hex(n)
    print(res[2:].upper())

num = int(input("Input your decimal number: "))
binary(num)
octal(num)
hexidecimal(num)
