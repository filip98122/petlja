a=int(input())
res=0
for i in range(a):
    b,c=map(int,input().split())
    res+=b-(b*(c/100))
print(round(res,2))