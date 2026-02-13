a,b=map(int,input().split())
res=0
for i in range(b-a+1):
    k=i+a
    l=[*str(k)]
    if k<0:
        del l[0]
    zbir=0
    for i1 in range(len(l)):
        zbir+=int(l[i1])
    if k!=0:
        if k%zbir==0:
            res+=1
print(res)