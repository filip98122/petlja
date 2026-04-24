a=int(input())
l=list(map(int,(input().strip()).split()))
res=0
for i in range(1,a):
    if l[i]<=l[i-1]:
        res+=(l[i-1]+1)-l[i]
        l[i]=l[i-1]+1
print(res)