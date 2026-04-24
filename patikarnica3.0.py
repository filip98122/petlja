a=int(input())
l=[]
reses={}
for i in range(a):
    b,c=(input().strip()).split()
    c=int(c)
    l.append(c)
    if f"{c}" in reses:
        reses[f"{c}"].append(b)
    else:
        reses[f"{c}"]=[b]
l.sort()
n=int(input())
for i in range(n):
    budget=int(input())
    lp=0
    rp=a-1
    if budget<l[0]:
        print("nema")
        continue
    if budget>=l[-1]:
        reses[f"{l[-1]}"].sort()
        for j in range(len(reses[f"{l[-1]}"])):
            print(reses[f"{l[-1]}"][j],l[-1])
        continue
    while True:
        mp=(lp+rp)//2
        if l[mp]<=budget and l[mp+1]>budget:
            reses[f"{l[mp]}"].sort()
            for j in range(len(reses[f"{l[mp]}"])):
                print(reses[f"{l[mp]}"][j],l[mp])
            break
        else:
            if l[mp]>budget:
                rp=mp
            else:
                lp=mp