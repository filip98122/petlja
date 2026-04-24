import math
l=list(map(str,(input().strip()).split()))
for i in range(len(l)):
    zapamti=l[i]
    res=0
    tren=l[i]
    for j in range(len(l[i])):
        if i>len(l[i])//2:
            res=len(l[i])
            break
        k=tren[0]
        tren=tren[1:]
        tren=tren+k
        res+=1
        if tren==zapamti:
            break
    l[i]=res
    
print(math.lcm(*l))