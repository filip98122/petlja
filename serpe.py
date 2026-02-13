l=list(map(int,input().split()))
l1=list(map(int,input().split()))
l.sort(reverse=True)
l1.sort(reverse=True)
res=0
for i in range(3):
    if l[0]>=l1[i]:
        res+=1
        del l[0]
print(res)