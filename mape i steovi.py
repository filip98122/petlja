l=list(map(int,input().split()))
nula=0
brojbeznule=1
ukupansum=1
for i in range(len(l)):
    if l[i]==0:
        nula+=1
    else:
        brojbeznule*=l[i]
    ukupansum*=l[i]
if nula>=2:
    print(("0 "*len(l)).strip())
else:
    li=[]
    for i in range(len(l)):
        if l[i]==0:
            li.append(brojbeznule)
        else:
            li.append(ukupansum/l[i])
    print(*li)