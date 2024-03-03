n = int(input())
List = list()
Req = list()
for _ in range(n):
    el = input()
    List.append(el)
k = int(input())
for _ in range(k):
    el_k = input()
    Req.append(el_k)
for i in range(len(List)):
    for j in range(len(Req)):
        if Req[j].lower() in List[i].lower():
            flag = True
        else:
            flag = False
            break
    if flag:
        print(List[i])