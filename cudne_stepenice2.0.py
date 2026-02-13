t= int(input())
l=list(map(int,input().split()))
prom=True
lis=[]
curent=0
poc=0
for i in range(t):
    if i==0:continue
    if prom:
        curent=l[i]-l[i-1]
        poc=i-1
        prom=False
    raz=l[i]-l[i-1]
    if curent!=raz:
        prom=True
        lis.append([poc,i-1])
    elif i==t-1:
        lis.append([poc,i-1])
najraz=0
iuraz=0
for i in range(len(lis)):
    tren=lis[i][1]-lis[i][0]
    if najraz<tren:
        iuraz=i
        najraz=tren
res=""
for i in range(len(l)):
    if lis[iuraz][0]<=i and lis[iuraz][1]>=i:
        res=res+str(l[i])
        res+=" "
print(res.strip())