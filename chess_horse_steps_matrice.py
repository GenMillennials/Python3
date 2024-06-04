# Chess horse steps visual
x, y = input()   # Coordinates in a chessboard with letter and number
n = 8            # Amount rows and columns on the chessbaord
M = [["."] * n for _ in range(8)]   # Filling in dots all chessboard
y = n - int(y)   # Transforming the number in the coordinate position of the chesshorse
x = ord(x) - 97  # Transforming the letter in the coordinate position of the chesshorse
M[y][x] = "N"    # The initial place of the chess horse location

for i in range(n):   # Iteration on the rows of chessboard
    for q in range(n):  # Iteration on the elements in the row of chessboard
        if abs(i - y) * abs(q - x) == 2:   # Checking the potential points of the chess horse steps -->
            M[i][q] = "*"   # --> Asterisks mark all potential positions

for m in range(n):   # The loop to iterate matrice rows
    print(*M[m])     # Output the result of this code
