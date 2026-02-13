a="abcdefghijklmnopqrstuvwxyz"
b=input().strip()
c=input().strip()
d={}
d2={}
for i in range(len(a)):
    d[a[i]]=0
    d2[a[i]]=0
for i in range(len(b)):
    d[b[i]]+=1
l=[]
for i in range(len(c)):
    d2[c[i]]+=1
for i in range(len(c)):
    l.append(d[c[i]]//d2[c[i]])
print(min(l))