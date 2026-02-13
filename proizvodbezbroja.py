a=int(input())
l=list(map(int,input().split()))
proizvod=1
nula=0
for i in range(len(l)):
    if l[i]==0:
        nula+=1
        if nula==2:
            proizvod=0
            break
        continue
    proizvod*=l[i]
res=[]
if nula==0:
    for i in range(len(l)):
        res.append(proizvod//l[i])
elif nula==2:
    for i in range(len(l)):
        res.append(0)
else:
    for i in range(len(l)):
        if l[i]==0:
            res.append(proizvod)
        else:
            res.append(0)
print(*res) 