vaucer,t1,t2=map(int,input().split())
lskija=[]
lpancerica=[]
for i in range(t1):
    lskija.append(int(input()))
for i in range(t2):
    lpancerica.append(int(input()))
lskija.sort()
lpancerica.sort()
lp=0
rp=t2-1
res=-1
while True:
    if rp==-1 or lp==t1:
        break
    zbir=lskija[lp]+lpancerica[rp]
    if zbir>vaucer:
        rp-=1
    else:
        if res<zbir:
            res=zbir
        lp+=1
print(vaucer-res)