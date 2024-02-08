class figure:
    def __init__(self, *p):
        self.p=p
    def print(self):
        print("figure")
        for el in self.p:
            el.print()
    def perimetr(self):
        f=True
        for el in self.p:
            if type(el) != point:
                f=False
        if f:
            return sum([distance(self.p[i], self.p[i-1]) for i in range(len(self.p))])
        else:
            return sum([el.perimetr() for el in self.p])


class point(figure):
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        self.p=[self]
    def print(self):
        print("point: x=", self.x, "y=", self.y)


class sector(figure):
    def __init__(self, A=point(0,0), B=point(0,0)):
        self.p=[A,B]
    def length(self):
        return distance(self.p[0], self.p[1])


def distance(A, B):
    return ((A.x - B.x)**2 + (A.y-B.y)**2) ** (1/2)


A=point(1,2)
A.print()
print(A.perimetr())
print()
B=figure(point(0,0), point(3,0), point(0,4))
B.print()
print(B.perimetr())
print()
B=sector(point(0,0), point(3,4))
B.print()
print(B.perimetr())
print(B.length())
print()
C=figure(figure(point(0,0), point(3,0), point(0,4), figure(point(10,10), point(13,10),
                                                           point(10,14)), figure(point(100,100), point(103,100), point(100,104))))
C.print()
print(C.perimetr())
print()