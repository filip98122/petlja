a,b=map(float,input().split())
a=int(a)
le=[]
ld=[]
for i in range(a):
    le.append(float(input())*b)
    ld.append(0)

p=int(input())
for i in range(p):
    lp,rp=map(float,input().split())
    for i in range(a):
        if lp-1<=i and rp-1>=i:
            ld[i]+=1
for i in range(a):
    if ld[i]>0 and le[i]>0:
        print(f"{le[i]/ld[i]:.2f}")
    else:
        print("0.00")