a = input()
l =[*a]
l1 = [0,1,2,3,4,5,6,7,8,9]
l2 = [9,8,7,6,5,4,3,2,1,0]
index1 = 0
index2 = 0
if len(l)==1:
    print(a)
    exit()
if len(l)==2:
    print(f"{l[1]}{l[0]}")
    exit()
for i in range(9,-1,-1):
    if str(i) in a:
        index2=a.rindex(str(i))
        if index2==0:
            continue
        break
    else:
        continue
for i in range(len(l)):
    if int(l[i])<int(l[index2]):
        index1=i
        break
temp1 = l[index1]
temp2 = l[index2]
l[index2] = temp1
l[index1] = temp2
res=""
prvibroj = False
for i in range(len(l)):
    if l[i]!="0":
        prvibroj=True
        res=res+l[i]
    else:
        if prvibroj==False:
            continue
        res=res+l[i]
print(res)