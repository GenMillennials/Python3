# def pascal_row(n: int):   # Announcing a function with one parameter - the certain row
#     if n == 0:        # If user wrote down the first row -->
#         return [1]    # --> This function returns [1] as a peak the Pascal's triangle
#     L = [[1]]         # Initialization a list with [1] value by default for row which more than 1 
#     for i in range(1, n + 1):   # Creating a row for each new "i" in loop, 
#         row = [1] * (i + 1)     # Creating row in length (i + 1) and the first and the end value its row equal 1
#         for j in range(i + 1):  # Creating a loop to iterate inner elements inside the row
#             if j != 0 and j != i:   # If each j not a null and not i (the first and the end elements) -->
#                 row[j] = L[i - 1][j - 1] + L[i - 1][j]   # --> The row is forming as a sum of two elements in the previous row in the L list
#         L.append(row)   # Addition the new row in the L list
#     return L[i]         # Returning L[i] as the end row which has been entered in n parameter

# num = int(input())      # Entered the user data in an integer
# print(pascal_row(num))      # Calling up the Pascal's function with the argument and the output it on a display

def pascal_triangle(n: int):   # Announcing a function with one parameter - the common row amount
    if n == 1:                 # If user wrote down the first row -->
        return [1]             # --> This function returns [1] as a peak the Pascal's triangle
    L = [[1]]                  # Initialization a list with [1] value by default for row which more than 1
    for i in range(1, n + 1):  # Creating a row for each new "i" in loop,
        row = [1] * (i + 1)    # Creating row on the full length (i + 1) and the first and the end value its row equal 1
        for j in range(i + 1): # Creating a loop to iterate inner elements inside the row
            if j != 0 and j != i:   # If each j not a null and not i (the first and the end elements) -->
                row[j] = L[i - 1][j - 1] + L[i - 1][j]   # --> The row is forming as a sum of two elements in the previous row in the L list
        L.append(row)          # Addition the new row in the L list
    return L[i - 1]            # Returning previous row with L[i - 1] value because row was used (n + 1) conditions in loop to create it

num = int(input())             # Entered the user data in an integer
for k in range(1, num + 1):    # Initialization a loop to iterate all row amount in the triangle
    print(pascal_triangle(k))  # Output the triangle in the list datatype which has been called the function