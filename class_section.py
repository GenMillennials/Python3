class point:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
    def input(self):
        s=[]
        s=input().split()
        self.x=float(s[0])
        self.y=float(s[1])
        return self


class section:
    def __init__(self, A=point(), B=point(1,0)):
        self.A=A
        self.B=B
    def input(self):
        self.A.input()
        self.B.input()
        return self
    def length(self):
        return(distance(self.A, self.B))


def distance(A, B):
    return((A.x - B.x)**2 + (A.y-B.y)**2) ** (0.5)


AB = section().input()
print(AB.length())