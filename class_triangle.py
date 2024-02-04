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


class triangle:
    def __init__(self, A=point(), B=point(), C=point()):
        self.A=A
        self.B=B
        self.C=C
    def input(self):
        self.A.input()
        self.B.input()
        self.C.input()
        return self
    def per(self):
        return(distance(self.A, self.B) + distance(self.B, self.C)) + distance(self.A, self.C)
    def square(self):
        p=self.per()/2
        return((p*(p-distance(self.A, self.B)) * (p-distance(self.B, self.C)) * (p-distance(self.A,self.C))) ** (0.5))



def distance(A,B):
    return((A.x - B.x)**2 + (A.y-B.y)**2) ** (0.5)


ABC= triangle().input()
print(ABC.per(), " ", ABC.square())