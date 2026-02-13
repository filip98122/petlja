a,b=map(int,input().split())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
if a==1:
    if abs(l[0]-l1[0])<b:
        print(1)
    else:
        print(0)
    exit()
l.sort()
l1.sort()
res=0
i1=0
i2=0
while i1!=a:
    if abs(l[i1]-l1[i2])<b:
        res+=1
        i1+=1
    elif l[i1]-l1[i2]<=-b:
        if i1==a-1:
            if i2==a-1:
                i1+=1
            else:
                i2+=1
        else:
            i1+=1
    else:
        if i2==a-1:
            i1+=1
        else:
            i2+=1
print(res)