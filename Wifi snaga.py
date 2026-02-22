a=int(input())
l1=list(map(int,input().split()))
b=int(input())
l2=list(map(int,input().split()))
res=0
for i in range(a):
    Lp=0
    Rp=a-1
    while True:
        Mp=(Lp+Rp)//2
        if  