a,b=map(int,input().split())
l=[]
for i in range(a):
    l.append(list(map(int,input().split())))
c,d=map(int,input().split())
posx=0
posy=0
res=0
while posx<b and posy<a:
    if l[posy][posx]==1:
        res+=1
    posx+=d
    posy+=c
print(res)