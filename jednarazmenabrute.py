k=int(input("Parameter1 "))
h=int(input("Parameter2 "))
for __ in range(k,h):
    a=str(__)
    l =[*a]
    if len(l)==1:
        continue
    if len(l)==2:
        continue
    l1 = [0,1,2,3,4,5,6,7,8,9]
    l2 = [9,8,7,6,5,4,3,2,1,0]
    index1 = 0
    index2 = 0
    remove=0
    for i in range(9,-1,-1):
        if str(i) in a:
            index2=a.rindex(str(i))
            if index2<=remove:
                continue
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

    l=[*a]
    bbbres=int(a)
    for i in range(len(l)):
        for j in range(i,len(l)):
            if j==i or int(l[i])>=int(l[j]):
                continue
            temp1 = l[i]
            temp2 = l[j]
            l[j] = temp1
            l[i] = temp2
            g="".join(l)
            if int(g)>bbbres:
                bbbres=int(g)
            l[i]=temp1
            l[j]=temp2
    if bbbres!=int(res):
        breakpoint()