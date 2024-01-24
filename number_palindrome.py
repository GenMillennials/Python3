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


""" def is_palindrome(n):  # Solving the task without string data type using
    x, y = n, 0      
    f = lambda: (y * 10) + x % 10 
    while x > 0:
        x, y = x // 10 , f()
    return y == n

print(is_palindrome(123454321))
print(is_palindrome(12)) """


n = int(input("Enter a number: "))  # Input a number from user
x = n  # Creating a new variable with duplicated number
y = 0  # Creating a variable for reversed number
while x > 0:  # While loop start. x variable will be reducing in the working while loop
    temp = x % 10  # Initialising temp variable to get last digit of the input number (its duplicate x)
    print(f"variable temp: {temp}")  # Checking the temp variable
    x = x // 10  # Deleting the last digit of the input number from its duplicate x
    print(f"variable x: {x}")  # Checking the x variable
    y = (y * 10) + temp  # Adding the last digit and adding a new digit in new reversed number
    print(f"variable y: {y}")  # Checking the y variable
print(y == n)  # Comparison reversed number and input number