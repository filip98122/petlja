a=int(input())
res=0
l=list(map(int,input().split()))
for i in range(a):
    if i==0:
        if l[i]>l[i+1]:
            res+=1
        continue
    if i==a-1:
        if l[i]>l[i-1]:
            res+=1
        continue
    if l[i]>l[i-1] and l[i]>l[i+1]:
        res+=1
print(res)