M=[[16,3,2,13],
   [5,10,11,8],
   [9,6,7,12],
   [4,15,14,1]]
print("The square is magic" if len(set([sum([M[i][i] for i in range(len(M))]),
    sum([M[i][-i-1] for i in range(len(M))])]
    +[sum(M[i]) for i in range(len(M))]
    +[sum([M[j][i] for j in range(len(M))]) for i in range(len(M))]))==1
    else "The square is ordinary")