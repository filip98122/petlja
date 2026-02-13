a,b=map(int,input().split())
res=0
for i in range(a,b+1):
    c=str(i)
    zbir=0
    for e in range(len(c)):
        if c[e]!="-":
            zbir+=int(c[e])
    if zbir!=0:
        if i%zbir==0:res+=1
print(res)