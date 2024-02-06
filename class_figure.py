class figure:
    def per(self):
        return 0
    def square(self):
        return 0
    def f_input(self):
        return self


class point(figure):
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def input(self):
        s=[]
        s=input().split()
        self.x=float(s[0])
        self.y=float(s[1])
        return self


class section(figure):
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


class triangle(figure):
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


class rectangle(figure):
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


s=input()
if s == "triangle":
    f = triangle()
elif s == "rectangle":
    f = rectangle()
elif s == "section":
    f = section()
elif s == "point":
    f = point()
else:
    f = figure()

f.input()
print(f.per(), "", f.square())