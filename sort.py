parni = []
neparni = []
__=int(input())
l=[]
for i in range(__):
    a = int(input())
    if a%2==1:
        neparni.append(a)
    else:
        parni.append(a)
neparni.sort()
parni.sort()
res=""
for i in range(len(parni)):
    res=res+str(parni[i])
    res=res+" "
    res=res+str(neparni[i])
    res=res+" "
print(res)