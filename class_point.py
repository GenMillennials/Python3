class point:
    def input(self):
        s=[]
        s=input().split()
        self.x=float(s[0])
        self.y=float(s[1])

def distance(A,B):
    return ((A.x - B.x) ** 2 + (A.y - B.y) ** 2) ** (0.5)


A = point()
B = point()
A.input()
B.input()
print(distance(A,B))