duzina,skracenje,broj_zvonca=map(int,input().split())
l = []

for i in range(broj_zvonca):
    res = 0
    d = int(input())
    l.append(d)

res = 0
for i in range(broj_zvonca):
    zvono = l[i]
    if zvono==0 or zvono==duzina:
        res = 1
    else:
        metoda1 = zvono // skracenje
        metoda2 = (duzina-zvono) // skracenje
        if metoda1<metoda2:
            res = metoda1*2
            res+=1#kad se vraca to je dvaput a ne samo 1 kao za sve ako je na desnoj polovini
            if (duzina-zvono)%skracenje==0:
                res-=1
        
        if metoda1>=metoda2:
            res = metoda2*2
            if (zvono)%skracenje==0:
                res-=1
        res+=1
    print(res)
