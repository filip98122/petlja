a,b=map(int,input().split())
x,y=0,0
l=[]
for i in range(a):
    l.append(list(map(int,input().split())))
proy,prox=map(int,input().split())
res=0
while x<b and y<a:
    if l[y][x]==1:
        res+=1
    x+=prox
    y+=proy
print(res)