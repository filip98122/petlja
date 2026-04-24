import math
l=list(map(str,(input().strip()).split()))
for i in range(len(l)):
    zapamti=l[i] # Current original word
    res=0 #kolko se do sada promenilo
    tren=l[i]
    nemoj=False
    
    new = zapamti+zapamti
    #for j in range(len(l[i])//2+1):
    #    # Shift
    #    k=tren[0]
    #    tren=tren[1:]
    #    tren=tren+k
    #    res+=1
    #    
    #    if tren==zapamti:
    #        nemoj=True
    #        break
    #if not nemoj:
    #    res=len(l[i])
    #l[i]=res
    l[i] = (new+new).find(new,1)
    
    #abababab
    
    
print(math.lcm(*l))