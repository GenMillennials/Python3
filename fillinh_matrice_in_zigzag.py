# Filling the matrice in a zigzag
s = input().split()
n, m = int(s[0]), int(s[1])
M = []
for _ in range(n):
    val = [0 for c in range(m)]
    M.append(val)
    
x, y = 0, 0
d_x, d_y = 0, 1
M[0][0] = 1
count = 2

while count <= n * m:
    if 0 <= x + d_x <= n - 1 and 0 <= y + d_y <= m - 1 and M[x + d_x][y + d_y] == 0:
        M[x + d_x][y + d_y] = count
        count += 1
        x += d_x
        y += d_y
    else:
        if d_y == 1:
            d_y = 0
            d_x = 1
        elif d_x == 1:
            d_x = 0
            d_y = -1
        elif d_y == -1:
            d_y = 0
            d_x = -1
        elif d_x == -1:
            d_x = 0
            d_y = 1
        
for i in range(n):
    for q in range(m):
        print(str(M[i][q]).ljust(3), end=" ")
    print()
