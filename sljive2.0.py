a=int(input())
p=(a//5)*2
d=(a//5)*3
t=a%5
res=0
if p>0:
    res+=1
if d>0:
    res+=1
if t>0:
    res+=1
print(p)
print(d)
print(t)
print(res)