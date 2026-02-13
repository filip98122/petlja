import random
for __ in range(1,101):
    a=__
    l=[]
    for i in range(a):
        l.append(random.randint(0,1))
    zbir=0
    parnih=[]
    neparnih=[]
    res=0
    for i in range(a):
        zbir+=l[i]
        if zbir%2==0:parnih.append(len(parnih))
        else:neparnih.append(len(neparnih))
    optimal=sum(neparnih)+sum(parnih)+len(parnih)
    res=0
    zbir=0
    for n in range(a):
        for i in range(n,a):
            zbir=0
            for j in range(n,i+1):
                zbir+=l[j]
            if zbir%2==0:res+=1
    if res!=optimal:
        breakpoint()