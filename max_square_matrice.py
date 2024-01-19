# Search the lenght of the biggest square inside a matrice (two-dimensional list).
# The square should be filled of nulls only.

def square(M,y=0,x=0,l=-1):  # Definiton a function consists of 4 parameters: Matrice, two coordinates and length of the square side
    if l==-1:
        l=len(M)
    f=True
    for i in range(y,y+1):
        for j in range(x,x+1):
            if M[i][j] != 0:
                f=False
                break
        if f==False:
            break
        if f==True:
            return l
        return max([square(M,y+1,x+1,l-1),
                    square(M,y,x+1,l-1),
                    square(M,y+1,x,l-1),
                    square(M,y,x,l-1)])

M=[[0,0,1,0,1],
   [1,0,0,0,0],
   [1,1,0,0,0],
   [0,0,0,0,0],
   [0,0,1,1,0]]

print(square(M))