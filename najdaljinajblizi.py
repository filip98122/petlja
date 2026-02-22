l=[]
for i in range(4):
    l.append(int(input()))
l.sort()
res=[]
raz=10000000
for i in range(4):
    if i==0:
        raz=l[1]-l[0]
        res=[l[0]]
        continue
    if i==3:
        razt=l[3]-l[2]
        if razt>raz:
            raz=razt
            res=[l[3]]
        elif razt==raz:
            res.append(l[3])
        continue
    razt=min(l[i]-l[i-1],l[i+1]-l[i])
    if razt>raz:
        raz=razt
        res=[l[i]]
    elif razt==raz:
        res.append(l[i])
for i in range(len(res)):
    print(res[i])