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


class rectangle:
    def __init__(self, A=point(), B=point()):
        self.A=A
        self.B=B
    def input(self):
        self.A.input()
        self.B.input()
        return self
    def per(self):
        return (2*(abs(self.B.x-self.A.x) + abs(self.B.y-self.A.y)))
    def square(self):
        return (abs(self.B.x-self.A.x) * abs(self.B.y-self.A.y))


def distance(A, B):
    return ((A.x-B.x) ** 2 + (A.y-B.y) ** 2) ** (0.5)


ABCD = rectangle()
ABCD.input()
print(ABCD.per(), " ", ABCD.square())