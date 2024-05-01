n = int(input())
L = [int(input()) for _ in range(n)]   # Or L = [int(input()) for k in range(int(input()))] without "n" variable above
mult = int(input())
flag = False
for i in range(len(L)):
    for j in range(len(L)):
        if L[i] * L[j] == mult and i != j:
            flag = True
            break
if flag:
    print("ДА")
else:
    print("НЕТ")