a=int(input())
l=list(map(int,input().split()))
res=0
if l[0]<l[1]:
    res+=1
if l[a-2]<l[a-1]:
    res+=1
for i in range(1,a-1):
    if l[i-1]<l[i] and l[i]<l[i+1]:
        res+=1
print(res)