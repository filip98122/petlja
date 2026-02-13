n=int(input())
l=list(map(int,input().split()))
res=0
if n==1:
    if sum(l)==0:
        res+=1
    print(res)
    exit()

suma=sum(l)
l.sort()
left=0
right=1
current=l[left]+l[right]
while True:
    if right==left or right==n:
        break
    if current==suma:
        res+=1
    if current>suma and left!=right-1 or n-right==1 and left!=right-1:
        current-=l[left]
        left+=1
    else:
        right+=1
        if right==left or right==n:
            break
        current+=l[right]
print(res)