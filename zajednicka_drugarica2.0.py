a=""
b=""
l=[]
for i in range(3):
    c,d=map(str,input().split())
    if i==0:
        a=c
        b=d
    l.append(c)
    l.append(d)
ares=0
bres=0

for i in range(len(l)):
    if l[i]==a:
        ares+=1
for i in range(len(l)):
    if l[i]==b:
        bres+=1
if ares==3:
    print(a)
elif bres==3:
    print(b)
else:
    print("nemoguce")