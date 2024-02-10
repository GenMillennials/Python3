class matrix:
    def __init__(self, n=1):
        self.n=n
        self.array=[]
        for i in range(n):
            self.array.append([0]*n)
    def __getitem__(self, i):
        return self.array[i]
    def __setitem__(self,i,v):
        self.array[i]=v
    def input(self):
        self.array=[[float(el) for el in input().split()] for i in range(self.n)]
        return self
    def print(self):
        for row in self:
            print(row)
        return self
    def __mul__(self, other):
        R=matrix(self.n)
        for i in range(self.n):
            for j in range(self.n):
                R[i][j] = self[i][j] * other[i][j]
        return R


A=matrix(2).input()
B=matrix(2).input()
C=A*B
C.print()