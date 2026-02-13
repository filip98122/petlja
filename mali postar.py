a=int(input())
l=list(map(int, input().split()))
levi=-1
desni=a
res=0
koj=True
l.sort()
while levi!=desni:
    if koj:
        levi+=1
        if levi==0:
            pass
        else:
            res+=abs(l[levi]-l[desni])
    else:
        desni-=1
        res+=abs(l[desni]-l[levi])
    if koj:
        koj=False
    else:
        koj=True
kuce=0
if koj:
    kuce=abs(l[levi]-l[0])
else:
    kuce=abs(l[desni]-l[0])
print(res+kuce)