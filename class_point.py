class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def input(self):
        s=[]
        s=input().split()
        self.x=float(s[0])
        self.y=float(s[1])
        return self


def distance(A,B):
    return ((A.x - B.x) ** 2 + (A.y - B.y) ** 2) ** (0.5)


A = point().input()
B = point().input()
print(distance(A,B))