# The chess queen steps on the chessboard visual
x, y = input()   # Coordinates of the point
n = 8            # The size of the chessboard is 8 x 8
M = [["."] * n for _ in range(8)]   # Filling the chessboard by dots
y = n - int(y)   # Getting the index of the chessboard column
x = ord(x) - 97  # Getting the index of numbmer from the letter row

for i in range(n):   # Iteration on the rows
    for q in range(n):   # Itereation on the elements
        if i == y or q == x:   # If the point is on the main or the secondary diagonal -->
            M[i][q] = "*"      # --> it marks by asterisk
        elif (i + q == y + x) or (i - q == y - x): # for the secondary diagonal
            M[i][q] = "*"      # -- "" -- "" --
        
M[y][x] = "Q"   # The strating point of the chess queen
for m in range(n):  # Iteration on chessboard
    print(*M[m])    # Output the chessboard with asterisks and the queen point