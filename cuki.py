a,b,c = map(int, input().split())
l = []
l1 = []
for i in range(c):
    res = 0
    d = int(input())
    l.append(d)
    l1.append(1)
lp = 0
rp = a
while True:
    lp+=b
    if lp == rp:
        break
    for i in range(c):
        if l[i]>=lp and l[i]<rp:
            l1[i]+=1
    rp-=b
    if lp == rp:
        break
    for i in range(c):
        if l[i]>lp and l[i]<=rp:
            l1[i]+=1
for i in range(c):
    print(l1[i])