class matrix:
    def __init__(self, n=1):
        self.n=n
        self.array=[]
        for i in range(n):
            self.array.append([0]*n)