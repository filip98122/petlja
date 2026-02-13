import math
a,b = map(int,input().split())
l=list(map(int,input().split()))
l.sort()
lastpresure=0
pressure=0
depth=l[0]-1
Rp=max(l)+math.ceil(b/a)
Mp=0
Lp=0
while Lp<Rp:
    lmp=Mp
    Mp=(Rp+Lp)//2
    
    lastdepth=depth
    depth=Mp
    pressure=0
    pressureplus1 = 0
    for i in range(len(l)):
        if l[i]<depth:
            pressureplus1+=depth-l[i]+1
        if l[i]<depth:
            pressure+=depth-l[i]
        else:
            break
        
    if pressure<=b and pressureplus1>b or lmp==Mp:
        print(Mp)
        break
    elif pressure<=b and pressureplus1<=b:
        Lp=Mp
    else:   
        Rp=Mp