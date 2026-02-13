a=int(input())
res=0
for i in range(a):
    l=list(map(int,input().split()))
    l.sort()
    res+=l[1]
print(res)