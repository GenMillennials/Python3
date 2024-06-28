# Different scores of three pupils

x1 = set(int(i) for i in input().split())   # Input the sequence of the first pupil
x2 = set(int(i) for i in input().split())   # Input the sequence of the second pupil
x3 = set(int(i) for i in input().split())   # Input the sequence of the third pupil

print(*sorted((x1 | x2 | x3) - (x1 & x2 & x3)))   # Output the sorted scores with a difference of union and interesection sets
