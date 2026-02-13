n=int(input())
l=list(map(int,input().split()))
if n==1 or n==2 or n==3:
    print(n)
    exit()
if n==4:
    cetiri=0
    for i in range(n):
        if l[i]%2==0:
            cetiri+=1
    if cetiri==4:
        print(3)
    else:
        print(n)
    exit()



lvalues=[]
parnih=0
parnihp=0
for i in range(n):
    if l[i]%2==0:
        l[i]=True
    else:
        l[i]=False
naj=0
left=0
right=1
trues=0
if l[0]:
    trues+=1
if l[1]:
    trues+=1
while right!=len(l)-1:
    if trues<=3:
        right+=1
        if l[right]:
            trues+=1
        if trues<=3:
            if naj<right-left+1:
                naj=right-left+1
    else:
        if l[left]:
            trues-=1
        left+=1
        if trues<=3:
            if naj<right-left+1:
                naj=right-left+1
print(max(naj,3))