a=int(input().strip())
l=list(map(int,(input().strip()).split()))
zbir=0
parnih=[]
neparnih=[]
res=0
for i in range(a):
    zbir+=l[i]
    if zbir%2==0:parnih.append(len(parnih))
    else:neparnih.append(len(neparnih))
print(sum(neparnih)+sum(parnih)+len(parnih))
#ko god ovo vidi, neka me sretne na okruznom
#posalje email na filip98122@gmail.com
#i dobije 5 dinara