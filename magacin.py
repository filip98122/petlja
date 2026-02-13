a = int(input())
l = list(map(int, input().split()))
l.sort()
res=0
while True:
    if l[-1]-l[0]>1:
        l[-1]-=1
        l[0]+=1
        l.sort()
        res+=1
    else:
        break
print(res)