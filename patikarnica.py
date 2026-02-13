n=int(input())
l={}
la=[]
for i in range(n):
    a,b=map(str,input().split())
    b=int(b)
    if f"{b}" in l:
        l[f"{b}"].append(a)
        l[f"{b}"].sort()
    else:
        l[f"{b}"]=[a]
    la.append(b)
la.sort()
k=int(input())
for i in range(k):
    a=int(input())
    if a<la[0]:
        print("nema")
        continue
    if a==la[0]:
        for j in range(len(l[str(a)])):
            print(f"{l[str(a)][j]} {a}")
        continue
    if a>=la[-1]:
        for j in range(len(l[str(la[-1])])):
            print(f"{l[str(la[-1])][j]} {la[-1]}")
        continue
    right=len(la)-1
    left=0
    res=0
    while True:
        if left==right-1:break
        middle=(right+left)//2
        if la[middle]==a:
            res=a
            break
        if la[middle]<a and la[middle+1]>a:
            res=la[middle]
            break
        try:
            
            if la[middle+1]==a:
                res=a
                break
        except:
            pass
        if la[middle-1]==a:
            res=a
            break
        if left==right-1:break
        if la[middle]<a:
            left=middle
        else:
            right=middle
    for j in range(len(l[str(res)])):
        print(f"{l[str(res)][j]} {res}")