# Search the lenght of the biggest square inside a matrice (two-dimensional list).
# The square should be filled of nulls only.

""" def square(M,y=0,x=0,l=-1,L=[]):
    if l==-1:
        l=len(M)
        L=[]
        for i in range(l+1):
            L.append([])
            for j in range(l+1):
                L[-1].append([-1]*(l+1))
    if L[y][x][l]==-1:
        f=True
        for i in range(y,y+1):
            for j in range(x,x+1):
                if M[i][j] != 0:
                    f=False
                    break
            if f==False:
                break
        if f==True:
            L[y][x][l]=1
        else:
            L[y][x][l]=max([square(M,y+1,x+1,l-1),
                    square(M,y,x+1,l-1),
                    square(M,y+1,x,l-1),
                    square(M,y,x,l-1)])
    return L[y][x][l]

M=[[0,0,1,0,1],
   [1,0,0,0,0],
   [1,1,0,0,0],
   [0,0,0,0,0],
   [0,0,1,1,0]]

print(square(M)) """

M = [[1, 1, 0, 0, 1],
     [0, 1, 0, 0, 0],
     [0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 1, 1, 0]]
L = list()
for y in range(len(M)):
    for x in range(len(M)):
        for l in range(len(M) - max(y, x) + 1):
            flag = True
            for i in range(y, y + 1):
                for j in range(x, x + 1):
                    if M[i][x + l - 1] != 0:
                        flag = False
                        break
            for j in range(x, x + 1):
                if M[y + l - 1][j] != 0:
                    flag = False
                    break
            if flag == True:
                L.append(l)
            else:
                break
print(max(L))