# Given an integer x, return true if x is a palindrome, and false otherwise.

""" number = input("Is a number palindrome? Input a number ")
if str(number) == str(number[::-1]):
    print(True)
else:
    print(False) """


""" def is_palindrome(number):
    string_number = str(number)
    return string_number == string_number[::-1]

print(is_palindrome(12345))
print(is_palindrome(11211))
print(is_palindrome(10134)) """


def is_palindrome(n):  # Solving the task without string data type using.
    x, y = n, 0      
    f = lambda: (y * 10) + x % 10 
    while x > 0:
        x, y = x // 10 , f()
    return y == n

print(is_palindrome(123454321))
print(is_palindrome(12))