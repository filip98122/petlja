h,t=map(int,input().split())
l=[]
for i in range(t):
    l.append(int(input()))
l.sort()
lp=0
rp=1
z1=0
z2=0
diff=0
while True:
    if rp==len(l):
        break
    a=l[rp]-l[lp]
    if a>h:
        lp+=1
        continue
    if a>diff:
        diff=a
        z1=l[lp]
        z2=l[rp]
    rp+=1
print(f"{z1} {z2}")