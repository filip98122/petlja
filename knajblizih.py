length,brojeva,x=map(int,input().split())
tren=list(map(int,input().split()))
l=[]
for i in range(length):
    l.append([abs(tren[i]-x),tren[i]])
l.sort()
res=[]
for i in range(brojeva):
    res.append(l[i][1])
res.sort()
print(*res)