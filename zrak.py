a,b = map(int,input().split())
l = []
for i in range(a):
    l1 = list(map(int,input().split()))
    l.append(l1)
c,d=map(int,input().split())
res = 0
xp = 0
yp = 0
prvo = 0
while xp<b and yp<a:
    if l[yp][xp]==1:
        res+=1
    prvo=1
    if prvo==1:
        xp+=d
        yp+=c
print(res)