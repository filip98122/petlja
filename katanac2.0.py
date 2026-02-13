a=input()
b=input()
res=0
for i in range(4):
    cilj=int(a[i])
    trenutni=int(b[i])
    if cilj==trenutni:
        continue
    copy=trenutni
    nadole=0
    nagore=0
    for j in range(20):
        copy-=1
        nadole+=1
        if copy==-1:
            copy=9
        if copy==cilj:
            break
    copy=trenutni
    for j in range(20):
        copy+=1
        nagore+=1
        if copy==10:
            copy=0
        if copy==cilj:
            break
    res+=min(nadole,nagore)
print(res)