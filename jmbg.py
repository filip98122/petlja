d1=input().strip()
d2=input().strip()
m1=input().strip()
m2=input().strip()
g1=input().strip()
g2=input().strip()
g3=input().strip()
d=int(d1+d2)
m=int(m1+m2)
g=g1+g2+g3
if g[0]=='0':
    g="2"+g
else:
    g="1"+g
g=int(g)
cd=15
cm=11
cg=2025
if cm>m:
    print(cg-g)
    exit()
if cm==m:
    if d<=cd:
        print(cg-g)
        exit()
print(cg-g-1)