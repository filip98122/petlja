a,b=map(int,(input().strip()).split())
res=0
for i in range(a,b+1):
    if i==0:
        continue
    zbir=0
    c=str(i)
    for j in range(len(c)):
        if c[j]=="-":
            continue
        zbir+=int(c[j])
    if i%zbir==0:
        res+=1
print(res)