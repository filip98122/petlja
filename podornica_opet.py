a,b = map(int,input().split())
import math
l=list(map(int,input().split()))
Rp=max(l)+math.ceil(b/a)
Mp=0
Lp=0
dictionary={}
for i in range(len(l)):
    if l[i] in dictionary:
        dictionary[l[i]]+=1
    else:
        dictionary[l[i]]=1
while Lp<Rp:
    lmp=Mp
    Mp=(Rp+Lp)//2
    if lmp==Mp:
        pressureplus2=0
        for i in dictionary:
            pressureplus2+=max((Mp+2)*dictionary[i]-i*dictionary[i],0)
            currentpressure+=max((Mp)*dictionary[i]-i*dictionary[i],0)
            pressureplus1+=max((Mp+1)*dictionary[i]-i*dictionary[i],0)
        if currentpressure<=b and pressureplus1>b:
            print(Mp)
            break
        if pressureplus1<=b and pressureplus2>b:
            print(Mp+1)
            break
    currentpressure=0
    pressureplus1=0
    for i in dictionary:
        currentpressure+=max(Mp*dictionary[i]-i*dictionary[i],0)
        pressureplus1+=max((Mp+1)*dictionary[i]-i*dictionary[i],0)
    if currentpressure<=b and pressureplus1>b:
        print(Mp)
        break
    elif currentpressure<=b and pressureplus1<=b:
        Lp=Mp
    else:   
        Rp=Mp