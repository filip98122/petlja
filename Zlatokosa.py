__ = int(input())
res=0
for i in range(__):
    l = list(map(int,input().split()))
    l.sort()
    res+=l[1]
print(res)