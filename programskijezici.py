n=int(input())
l={}
listl=[]
lk=[]

preskaci=0
for i in range(n):
    da=False
    a,b=map(str,input().split())
    b=int(b)
    lk.append([a,b])
    try:
        if l[a]=="":
            pass
        da=True
    except:
        pass
    if da==False:
        l[a]=b
        l[f"{a}p"]=1
    else:
        l[a]+=b
        l[f"{a}p"]+=1
    if l[f"{lk[i][0]}p"]==1:
        listl.append(lk[i][0])
        #l[f"{lk[i][0]}p"]]
listl.sort()
for i in range(len(listl)):
    print(f"{listl[i]} {'{0:.2f}'.format(l[listl[i]]/l[f"{listl[i]}p"])}")
