l=[0,0,0,0,0,0,0,0]
for i in range(int(input())):
    a,b=map(float,input().split())
    a=int(a)
    if b>=4.50:
        l[a-1]+=1
res=0
naj=-1
for i in range(8):
    if l[i]>=naj:
        res=i+1
        naj=l[i]
print(res)