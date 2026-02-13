l=list(map(int,input().split()))
res=0
__=int(input())
for i in range(__):
    l1 = list(map(int,input().split()))
    if l[0]<=l1[0] and l[1]<=l1[1] and l[2]<=l1[2]:
        res+=1
print(res)