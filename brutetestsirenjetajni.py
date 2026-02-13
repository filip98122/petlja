import random
edge1=int(input("Ucenika 1 "))
edge2=int(input("Ucenika "))
edge3=int(input("Pratioca 1 "))
edge4=int(input("Pratioca "))
edge5=int(input("Rasporeda 1 "))
edge6=int(input("Rasporeda "))
for jk in range(edge1,edge2):
    ucenika=jk
    pozprat=[]
    pratiocib=random.randint(edge3,edge4)
    for i in range(pratiocib):
        while True:
            h=random.randint(1,jk)
            if h not in pozprat:
                pozprat.append(h)
                break
    
    rasporeda=random.randint(edge5,edge6)
    pozprat.sort()
    for i in range(rasporeda):
        while True:
            h=random.randint(1,jk)
            if h not in pozprat:
                a=h
                break
        if a<pozprat[0]:
            continue
        if a>pozprat[-1]:
            continue
        left=0
        right=len(pozprat)-1
        while True:
            mid=(right+left)//2
            if mid+1==len(pozprat):
                val=ucenika+1
            else:
                val=pozprat[mid+1]
            if pozprat[mid]<a<val:
                res=val-pozprat[mid]-1
                break
            if left==right-1:
                break
            if pozprat[mid]>a:
                right=mid
            else:
                left=mid
        for i in range(len(pozprat)):
            if pozprat[i]<a:
                continue
            else:
                if i==0:
                    val=0
                else:
                    val=pozprat[i-1]
                resb=pozprat[i]-val-1
                break
        if resb != res:
            breakpoint()
        print(res,resb)