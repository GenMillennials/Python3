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


M=matrix(2)
M.input()
M.print()