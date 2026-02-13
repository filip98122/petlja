a = input().strip()
l =[*a]
if len(l)==1:
    print(a)
    exit()
if len(l)==2:
    print(max(int(f"{l[1]}{l[0]}"),int(a)))
    exit()
l1 = [0,1,2,3,4,5,6,7,8,9]
l2 = [9,8,7,6,5,4,3,2,1,0]
index1 = 0
index2 = 0
remove=0
for i in range(9,-1,-1):
    if str(i) in a:
        index2=a.rindex(str(i))
        if index2==0:
            continue
        mala=l[0:index2]
        q=False
        for m in range(i-1,-1,-1):
            if str(m) in mala:
                q=True
                break
        if q:
            break
    else:
        continue
for i in range(len(l)):
    if index2>i:
        if int(l[i])<int(l[index2]):
            index1=i
            break
    elif index2<i:
        if int(l[i])>int(l[index2]):
            index1=i
            break
temp1 = l[index1]
temp2 = l[index2]
l[index2] = temp1
l[index1] = temp2
res="".join(l)
if res<a:
    res=a
print(res)