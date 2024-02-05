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


class triangle:
    def __init__(self, A=point(), B=point(), C=point()):
        self.A=A
        self.B=B
        self.C=C
        self.onChange()
    def input(self):
        self.A.input()
        self.B.input()
        self.C.input()
        self.onChange()
        return self
    def onChange(self):
        self.AB=section(self.A, self.B)
        self.BC=section(self.B, self.C)
        self.AC=section(self.A, self.C)
    def per(self):
        return(self.AB.length() + self.BC.length() + self.AC.length())
    def square(self):
        p=self.per()/2
        return((p*(p-self.AB.length())) * (p-self.BC.length()) * (p-self.AC.length()) ** (0.5))



def distance(A,B):
    return((A.x - B.x)**2 + (A.y-B.y)**2) ** (0.5)


ABC= triangle().input()
print(ABC.per(), " ", ABC.square())