a,b= map(int, input().split())
prosek = 0
l = []
for i in range(a):
    c = int(input())
    l.append(c)
    prosek+=c
prosek/=a
g = 0
for i in range(a):
    if l[g]<prosek:
        del l[g]
        g-=1
    g+=1
broj = ""
for i in  range(len(l)):
    l[i] = str(l[i])
    broj=broj+l[i]
broj = int(broj)
broj*=b
print(broj)
res=0
count =0
broj=str(broj)
l=[*broj]
for i in range(len(l)-1,-1,-1):
    if count==0:
        res+=int(l[i])
        count=1
    else:
        res-=int(l[i])
        count=0
print(res)