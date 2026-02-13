a=int(input())
l=[*input()]
lsam=["a","e","i","o","u"]
res=[]
for i in range(a):
    current=l[i]
    breaksure=False
    for j in range(5):
        if current.lower()==lsam[j]:
            breaksure=True
    if breaksure==False:
        res.append(current)
print(len(res))
