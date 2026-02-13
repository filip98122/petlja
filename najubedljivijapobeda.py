t=int(input().strip())
res=0
for i in range(t):
    a,b=map(int,(input().strip()).split())
    if abs(a-b)>res:
        res=abs(a-b)
print(res)
