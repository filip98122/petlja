duz,skrc,zvnca=map(int,input().split())
for i in range(zvnca):
    res=0
    zvono=int(input())
    levo=zvono//skrc
    desno=(duz-zvono)//skrc
    if zvono==0 or zvono==duz:
        print(1)
        continue
    if levo<=desno:
        res+=levo*2
        if (zvono)%skrc==0:
            res-=1
    else:
        res+=desno*2+1
        if (duz-zvono)%skrc==0:
            res-=1
    print(res+1)