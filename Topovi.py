n=int(input())
l1=[]
for i in range(n):
    l=list(map(int,input().split()))
    if sum(l)>1:
        print(1)
        exit()
    for ii in range(n):
        if i==0:
            l1.append(l[ii])
            continue
        l1[ii]+=l[ii]
        if l1[ii]>1:
            print(1)
            exit()
print(0)