a,b=map(float,input().split())
a=int(a)

le=[]
ldays=[]

for i in range(a):
    le.append(float(input())*b)
    ldays.append(0)

p=int(input())

for i in range(p):
    lp,rp=map(int,input().split())
    for j in range(a):
        if lp<=j+1 and j+1<=rp:
            ldays[j]+=1

for i in range(len(ldays)):
    if ldays[i]>0 and le[i]>0:
        print(f"{le[i]/ldays[i]:.2f}")
    else:
        print("0.00")