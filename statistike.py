__ = int(input())
resu=0
for i in range(__):
    res = 0
    l=list(map(int, input().split()))
    for ii in range(5):
        if l[ii]>=10:
            res+=1
    if res>=3:
        resu+=1
print(resu)