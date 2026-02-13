a2=int(input())
a,b=map(int,input().split())
a1,b1=map(int,input().split())
l=[]
for i in range(1,a2):
    if i==a:
        l.append(b)
    if i==a1:
        if len(l)==i:
            l.append(b1)
        l.append(b1)
    