a=int(input())
res=0
for i in range(a):
    l=list(map(int,input().split()))
    da=0
    for j in range(5):
        if l[j]>9:
            da+=1
    if da>2:
        res+=1
print(res)