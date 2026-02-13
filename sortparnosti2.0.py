a=int(input())
parnih=[]
neparnih=[]
for i in range(a):
    b=int(input())
    if b%2==0:
        parnih.append(b)
    else:
        neparnih.append(b)
parnih.sort()
neparnih.sort()
l=[]
for i in range(len(parnih)):
    l.append(parnih[i])
    l.append(neparnih[i])
print(*l)