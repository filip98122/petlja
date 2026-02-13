a,b,c = map(int, input().split())
skije = []
for i in range(b):
    skije.append(int(input()))
pancerice = []
for i in range(c):
    pancerice.append(int(input()))

l = 0
r = c-1
skije.sort()
pancerice.sort()
rez = 0
while l<b and r>=0:
    cena = skije[l]+pancerice[r]
    if cena > a:
        r-=1
    else:
        rez = max(rez,cena)
        l+=1
print(a-rez)