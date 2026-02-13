l11=input()
l22=input()
l1=[]
l2=[]
for i in range(len(l11)):
    l1.append(int(l11[i]))
    l2.append(int(l22[i]))
res1=0
res2=0
counter=0
for i in range(len(l1)):
    if l1[counter]==l2[counter]:
        res1+=1
        del l1[counter]
        del l2[counter]
        continue
    counter+=1
d={}
for i in range(10):
    d[f"{i}"]=[0,0]
for i in range(len(l1)):
    d[f"{l1[i]}"][0]+=1
    d[f"{l2[i]}"][1]+=1
for i in range(10):
    res2+=min(d[f"{i}"])
print(res1,res2)